from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Category
from django.contrib import messages
from user_profile.models import Profile

# Create your views here.
def home(request):
    rooms = Room.objects.all().order_by('-updated')
    context = {"rooms": rooms}
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
        room_name = request.POST['room_name']
        room_category = request.POST['room_topic']
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
    
    categories = Category.objects.all()
    context = {"rooms": rooms,
               "categories":categories}
    return render(request, 'chat_app/home.html', context)

def filter_mobile(request):
    """ for mobile view """
    return render(request, 'chat_app/filter.html')

def video_stream(request):
    """ view function for stream """
    return render(request, 'chat_app/video-room/video-room.html')