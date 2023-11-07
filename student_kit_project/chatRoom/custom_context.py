from user_profile.models import Profile 
from chatRoom.models import Room_Members
from django.contrib.auth.models import AnonymousUser

def common_context(request):
    user = None

    if request.user and not isinstance(request.user, AnonymousUser):
        try:
            user = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass
    
    return {
        "user": user,
    }
