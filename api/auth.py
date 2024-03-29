from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED)
from rest_framework.response import Response

from common.models import User
from .serializers import UserSerializer, UserSigninSerializer, UserSignUpSerializer
from .authentication import token_expire_handler, expires_in


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    serialized = UserSignUpSerializer(data=request.data)
    if serialized.is_valid():
        user = User.objects.create_user(
            serialized.data['username'],
            serialized.data['email'],
            serialized.data['password']
        )
        # TOKEN STUFF
        token, _ = Token.objects.get_or_create(user=user)

        # token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = token_expire_handler(token)  # The implementation will be described further
        user_serialized = UserSerializer(user)

        return Response({
            'result': True,
            'data': {
                'user': user_serialized.data,
                'token': token.key
            }
        }, status=HTTP_201_CREATED)
    else:
        return Response({
            'result': False,
            'error': serialized._errors
        }, status=HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((AllowAny,))
def signin(request):
    signin_serializer = UserSigninSerializer(data=request.data)
    if not signin_serializer.is_valid():
        return Response({
            'result': False,
            'error': signin_serializer.errors
        }, status=HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=signin_serializer.data['username'],
        password=signin_serializer.data['password']
    )
    if not user:
        return Response({
            'result': False,
            'error': {'detail': 'Invalid Credentials or activate account'}
        }, status=HTTP_404_NOT_FOUND)

    # TOKEN STUFF
    token, _ = Token.objects.get_or_create(user=user)

    # token_expire_handler will check, if the token is expired it will generate new one
    is_expired, token = token_expire_handler(token)  # The implementation will be described further
    user_serialized = UserSerializer(user)

    return Response({
            'result': True,
            'data': {
                'user': user_serialized.data,
                'token': token.key
            }
        }, status=HTTP_200_OK)


@api_view(["GET"])
def user_info(request):
    return Response({
        'user': request.user.username,
        'expires_in': expires_in(request.auth)
    }, status=HTTP_200_OK)
