from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('edith_profile', views.edith_profile, name="edith_profile"),

]
