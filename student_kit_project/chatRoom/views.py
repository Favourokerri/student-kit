from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Category, Room_Members
from django.contrib import messages
from user_profile.models import Profile
from agora_token_builder import RtcTokenBuilder
import os
import time, random

# Create your views here.
def room_search(request):
    query = request.GET.get('q', '')
    rooms = Room.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'rooms': rooms,
    }
    return render(request, 'chat_app/home.html', context)

def home(request):
    rooms = Room.objects.all().order_by('-updated')
    total_active_rooms = Room.objects.filter(active=True).count()
    total_room = Room.objects.count()
    context = {"rooms": rooms,
               "total_room":total_room,
               'total_active_rooms':total_active_rooms}
    return render(request, 'chat_app/home.html', context)

def room(request, room_id):
    rooms = Room.objects.get(id=room_id)
    context={"rooms": rooms}
    return render(request, 'chat_app/room.html', context)

def recent_activity(request):
    return render(request, 'chat_app/recent_activity.html')

def create_room(request):
    """ function for craeting of view"""
    categories = Category.objects.all()
    profile = Profile.objects.get(user=request.user)
    context = {"categories": categories}
    if request.method == 'POST':
        room_name = request.POST['room_topic']
        room_category = request.POST['room_name']
        description = request.POST['room_about']

        category, created = Category.objects.get_or_create(name=room_category)
        room = Room.objects.create(host=request.user,
                                   host_profile=profile,
                                    category=category,
                                    name=room_name,
                                    description=description,
                                    )
        category.save()
        room.save()
        messages.success(request, 'room created successfully')
        return redirect('chat_home')

    return render(request, 'chat_app/create_room.html', context)

def edith_room(request, room_id):
    room = Room.objects.get(host=request.user, id=room_id)

    try:
        if request.method == "POST":
            room_name = request.POST['room_name']
            room_category = request.POST['room_topic']
            description = request.POST['room_about']

            room.name = room_name
            room.category, create = Category.objects.get_or_create(name=room_category)
            room.description = description
            room.save()
            messages.success(request, "room updated successfully")
            return redirect("chat_home")

    except Room.DoesNotExist:
            messages.warning(request, "this room has been deleted")
            return redirect('chat_home')
    
    context = {"room":room}
    return render(request, "chat_app/edith_room.html", context)     

def delete_room(request, room_id):
    try:
        room = Room.objects.get(host=request.user, id=room_id)
    except Room.DoesNotExist:
        messages.warning(request, "this room has been deleted")
        return redirect('chat_home')
    
    if request.method == "POST":
        room.delete()
        messages.success(request, 'room deleted successfully')
        return redirect('chat_home')
    context = {"room": room}
    return render(request, 'chat_app/confirm_delete.html', context)

def filter_room(request, action):
    if action == "all":
        rooms = Room.objects.all().order_by('-updated')
    elif action == "my_created_rooms":
        rooms = Room.objects.filter(host=request.user)
    elif action == 'active_rooms':
        rooms = Room.objects.filter(active=True)
    
    categories = Category.objects.all()
    context = {"rooms": rooms,
               "categories":categories}
    return render(request, 'chat_app/home.html', context)

def filter_mobile(request):
    """ for mobile view """
    return render(request, 'chat_app/filter.html')

def join_video_stream(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
        appId='f055d16d5cb9403493bf2f68ba29d67a'
        appCertificate='dcde3281bbc649e1b761478c5e303a5b'
        channelName=room.name
        user_id = request.user.id
        user = request.user.first_name  # Get the user's unique ID
        role=1
        current_time = int(time.time())
        privilegeExpiredTs = current_time + 3600
        token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, user_id, role, privilegeExpiredTs)

        room_members = Room_Members.objects.create(user=request.user, room=room)
        room_members.save()
        
        if not room.active: #code for marking room active if users are present
            room.active=True
            room.save()
    except Room.DoesNotExist:
        messages.warning(request, 'this room may have been deleted')
        return redirect('chat_home')
   
    context = {
        'token': token,
        'user_id': user_id,
        'room': room,
        'user1': user,
    }
    return render(request, 'chat_app/video-room/video-room.html', context)

def leave_video_stream(request, room_id):
    """ 
        models for leaving room.
        we will also handel marking room as inactive
    """
    try:
        room_member = Room_Members.objects.filter(user=request.user, room__id=room_id)
        room_member.delete()

        get_room_members = Room_Members.objects.filter(room_id=room_id)
        if not get_room_members: #code for marking room inactive
            room = Room.objects.get(id=room_id)
            room.active = False
            room.save()
        messages.success(request, 'you left the room')
    except Room_Members.DoesNotExist:
          messages.warning(request, 'you already left the room')
    return redirect('chat_home')