from django.urls import path
from chatRoom import views

urlpatterns = [
    path('search/', views.room_search, name='room_search'),
    path('home', views.home, name='chat_home'),
     path('recent_activity', views.recent_activity, name='recent_activity'),
    path('room/<int:room_id>/', views.room, name='room'),
    path('create_room', views.create_room, name='create_room'),
    path('filter_room/<str:action>/', views.filter_room, name='filter_room'),
    path('filter_room_mobile', views.filter_mobile, name='filter_room_mobile'),
    path('edith_room/<int:room_id>/', views.edith_room, name="edith_room"),
    path('delete_room/<int:room_id>/', views.delete_room, name="delete_room"),
    path('video-stream/<int:room_id>/', views.join_video_stream, name="join_video-stream"),
    path('leave-video-stream/<int:room_id>/', views.leave_video_stream, name="leave_video-stream"),
]