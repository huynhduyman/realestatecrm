from django.urls import path, include
from rest_framework import routers

from . import views, auth
from .views import UserListCreateAPIView, UserDetailUpdateAPIView

router = routers.SimpleRouter()
# router.register(r'user', UserListCreateAPIView, base_name="User")     # đăng ký API vào router
router.register(r'user', UserDetailUpdateAPIView, base_name="User")

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/signup', auth.signup, name="signup"),
    path('v1/signin', auth.signin, name="signin"),
    path('v1/signin', auth.user_info, name="user_info"),
    path('v1/user_info', auth.user_info, name="user_info"),
    path('v1/predict', views.predict, name="predict"),
    path('v1/create_lead_from_site', views.create_lead_from_site,
         name='create_lead_from_site'),
    path('v1/create_case_from_site', views.create_case_from_site,
         name='create_case_from_site'),
]