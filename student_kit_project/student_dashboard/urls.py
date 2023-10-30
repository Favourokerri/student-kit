from django.urls import path
from student_dashboard import views

urlpatterns = [
    path('student', views.index, name='dash_board')
]