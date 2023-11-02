from django.urls import path
from chatRoom import views

urlpatterns = [
    path('home', views.home, name='chat_home'),
     path('recent_activity', views.recent_activity, name='recent_activity'),
    path('room/<uuid:room_id>/', views.room, name='room'),
    path('create_room', views.create_room, name='create_room'),
    path('filter_room/<str:action>/', views.filter_room, name='filter_room'),
    path('filter_room_mobile', views.filter_mobile, name='filter_room_mobile'),
    path('edith_room/<uuid:room_id>/', views.edith_room, name="edith_room"),
    path('delete_room/<uuid:room_id>/', views.delete_room, name="delete_room"),
    path('vider-stream', views.video_stream, name="video-stream"),
]