import pickle

import numpy as np
import pandas as pd
from coverage.python import os
from django.http import JsonResponse
from rest_framework import status, serializers
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView, )
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from sklearn.externals import joblib

from django.contrib.sites.shortcuts import get_current_site

from api.serializers import UserSerializer, UserUpdateSerializer
from common.models import User
from leads.models import Lead
from opportunity.models import Opportunity
from cases.models import Case
from listings.models import Listing
from crm.settings import BASE_DIR
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserListSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default="USER")
    has_sales_access = serializers.BooleanField(default=False)
    has_marketing_access = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = 'id', 'username', 'first_name', 'last_name', 'email', 'role', 'is_active', 'has_sales_access', \
                 'has_marketing_access'


# API get detail, update, delete
class UserDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'

    # permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_serialize = UserUpdateSerializer(data=request.data)
        if not user_serialize.is_valid():
            return Response({
                'result': False,
                'error': user_serialize.errors
            }, status=HTTP_404_NOT_FOUND)

        users = User.objects.filter(id=kwargs['id'])
        if len(users) == 0:
            return Response({
                'result': False,
                'error': {'detail': 'user not found'}
            }, status=HTTP_404_NOT_FOUND)

        user = users[0]
        user.first_name = user_serialize.data['first_name']
        user.last_name = user_serialize.data['last_name']
        user.role = user_serialize.data['role']
        user.has_sales_access = user_serialize.data['has_sales_access']
        user.has_marketing_access = user_serialize.data['has_marketing_access']
        user.save()
        user_serialize = UserUpdateSerializer(user)
        return Response({
            'result': True,
            'data': user_serialize.data
        }, status=HTTP_200_OK)


# API get list and create
class UserListCreateAPIView(viewsets.GenericViewSet,
                            CreateAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]
    role = "USER"


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def predict(request):
    try:
        pkl_filename = os.path.join(BASE_DIR, 'pkl/phu_nhuan_pickle_model.pkl')
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)

        # Calculate the accuracy score and predict target values
        mydata = request.data
        x_test = [mydata['dienTich'], mydata['phongNgu'], mydata['phongTam'], mydata['tang'], mydata['internal_roads'],
                  mydata['hemxehoi'], mydata['house_width'], mydata['ground_floors'], mydata['terraces'], mydata['lat'],
                  mydata['long']]
        # x_test = np.array(a)
        # score = pickle_model.score(x_test, y_test)
        # print("Test score: {0:.2f} %".format(100 * score))
        # print(x_test)
        predicts = pickle_model.predict([x_test])
        response = {}
        data = {}

        if len(predicts) > 0:
            predict = float(predicts[0])
            response['result'] = True
            gia = float(mydata.get('gia', False))
            if gia:
                score = gia / predict
                if score > 1:
                    score = 1 / score
                data['score'] = round(score, 2)

            data['predict'] = predict
            response['data'] = data
        else:
            response['result'] = False
            response['message'] = "Cannot predict"

        return Response(response, status.HTTP_200_OK)

    except BaseException as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_case_from_site(request): # pragma: no cover
    try:
        getdata = request.data
        #print(getdata)
        #print(request.method)
        response = {}
        #data = {}

        allowed_domains = ['ihomereal.com', 'agent.ihomereal.com', 'localhost:8000', ]
        # add origin_domain = request.get_host() in the post body
        if (request.get_host() in ['localhost:8000', 'agent.ihomereal.com', ] and getdata['origin_domain'] in allowed_domains):
            if request.method == 'POST':
                if getdata['full_name']:
                    lead = Lead.objects.create(title=getdata['full_name'], email=getdata[
                        'email'], phone=getdata['phone'], description=getdata['message'],
                        created_from_site=True)
                    recipients = User.objects.filter(
                        role='ADMIN').values_list('id', flat=True)
                    lead.assigned_to.add(*recipients)
                    from leads.tasks import send_email_to_assigned_user
                    send_email_to_assigned_user(
                        recipients, lead.id, domain='agent.ihomereal.com', protocol='https',
                        source=getdata['origin_domain'])
                    response['message'] = "Lead Created"
                    # Create Case
                    if getdata['case']:
                        print('co case')
                        
                        created_by = request.user
                        
                        case = Case.objects.create(name='case from site', 
                            status=getdata['status'], 
                            case_type=getdata['case_type'],
                            priority=getdata['priority'],
                            created_by=created_by,
                            closed_on=getdata['closed_on'],
                            description=getdata['message'])
                        print(case)
                        case.assigned_to.add(*recipients)
                        #opportunity.created_by.add('1')
                        case.leads.add(lead.id)
                        #case.listings.add(getdata['listing_id'])
                        # send email assign usser opportunity
                        #current_site = get_current_site(request)
                        from cases.tasks import send_email_to_assigned_user
                        send_email_assign_case = send_email_to_assigned_user(
                            recipients, case.id, 
                            domain='agent.ihomereal.com', 
                            protocol='https')
                        response['message'] += ", Case Created"
                        #print(send_email_assign_opportunity)
                    response['result'] = True
                    response['message'] = response['message']
        else:
            response['result'] = False
            response['message'] = "Cannot Lead, Domain not accepted"

        return Response(response, status.HTTP_200_OK)

    except BaseException as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_lead_from_site(request): # pragma: no cover
    try:
        getdata = request.data
        #print(getdata)
        #print(request.method)
        response = {}
        #data = {}

        allowed_domains = ['ihomereal.com', 'localhost:8000', ]
        # add origin_domain = request.get_host() in the post body
        if (request.get_host() in ['localhost:8000', 'agent.ihomereal.com', ] and getdata['origin_domain'] in allowed_domains):
            if request.method == 'POST':
                if getdata['full_name']:
                    lead = Lead.objects.create(title=getdata['full_name'], email=getdata[
                        'email'], phone=getdata['phone'], description=getdata['message'],
                        created_from_site=True)
                    recipients = User.objects.filter(
                        role='ADMIN').values_list('id', flat=True)
                    lead.assigned_to.add(*recipients)
                    from leads.tasks import send_email_to_assigned_user
                    send_email_to_assigned_user(
                        recipients, lead.id, domain='agent.ihomereal.com', protocol='https',
                        source=getdata['origin_domain'])
                    response['message'] = "Lead Created"
                    # Create opportunity
                    if getdata['opportunity']:
                        print('co co hoi')
                        created_by = request.user
                        opportunity = Opportunity.objects.create(name='opportunity from site', 
                            stage=getdata['stage'], 
                            currency='VND', 
                            amount=getdata['amount'],
                            lead_source='WEBSITE',
                            probability=getdata['probability'],
                            created_by=created_by,
                            description=getdata['message'])
                        opportunity.assigned_to.add(*recipients)
                        #opportunity.created_by.add('1')
                        opportunity.leads.add(lead.id)
                        opportunity.listings.add(getdata['listing_id'])
                        # send email assign usser opportunity
                        #current_site = get_current_site(request)
                        from opportunity.tasks import send_email_to_assigned_user
                        send_email_assign_opportunity = send_email_to_assigned_user(
                            recipients, opportunity.id, 
                            domain='agent.ihomereal.com', 
                            protocol='https')
                        response['message'] += ", Opportunity Created"
                        #print(send_email_assign_opportunity)
                    response['result'] = True
                    response['message'] = response['message']
        else:
            response['result'] = False
            response['message'] = "Cannot Lead, Domain not accepted"

        return Response(response, status.HTTP_200_OK)

    except BaseException as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)