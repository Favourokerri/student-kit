from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('verify/<str:auth_token>/', views.verify_account, name='verify_account'),
    path('resend_token', views.resend_verification, name='resend_verification')
]