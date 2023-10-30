from django.urls import path
from notification import views

urlpatterns = [
    path('notification', views.notification, name='notification'),
    path('mark_read', views.mark_read, name='read_notifications'),
]