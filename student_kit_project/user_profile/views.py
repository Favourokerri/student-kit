from django.shortcuts import render
from chatRoom.models import Room
from .models import Profile
from django.contrib import messages

# Create your views here.\
def profile(request):
    rooms = Room.objects.filter(host=request.user)
    context={"rooms":rooms}
    return render(request, 'chat_app/profile.html', context)

from django.shortcuts import render, redirect
from .models import Profile

def edith_profile(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)

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
 
    return render(request, 'chat_app/edith_profile.html')