from rest_framework import serializers

from common.models import User


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(default="")
    last_name = serializers.CharField(default="")
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'role', 'has_sales_access', 'has_marketing_access'


class UserSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = 'username', 'email', 'password'


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    role = serializers.CharField(default="USER")
    has_sales_access = serializers.BooleanField(default=False)
    has_marketing_access = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = 'id', 'username', 'first_name', 'last_name', 'email', 'role', 'is_active', 'has_sales_access', \
                 'has_marketing_access'
        write_only_fields = 'password',