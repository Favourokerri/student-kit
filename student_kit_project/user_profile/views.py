from django.shortcuts import render
from chatRoom.models import Room, Room_Members
from .models import Profile
from django.contrib import messages

# Create your views here.\
def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    rooms = Room.objects.filter(host_profile=profile)
    total_active_rooms = Room.objects.filter(active=True).count()
    members_count=Room_Members.objects.count()
    context={"rooms":rooms,
             "profile": profile,
             "members_count":members_count,
             "total_active_rooms":total_active_rooms}
    return render(request, 'chat_app/profile.html', context)

from django.shortcuts import render, redirect
from .models import Profile

def edith_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        # Update the profile fields with form data
        if 'profile_pic' in request.FILES:
            profile.profile_image = request.FILES['profile_pic']
        if 'first_name' in request.POST:
            profile.first_name = request.POST['first_name']
        if 'last_name' in request.POST:
            profile.last_name = request.POST['last_name']
        if 'user_bio' in request.POST:
            profile.bio = request.POST['user_bio']
        profile.save()
        messages.success(request, 'profile edithed successfully')
        return redirect('chat_home')
    context = {'profile': profile}
    return render(request, 'chat_app/edith_profile.html', context)