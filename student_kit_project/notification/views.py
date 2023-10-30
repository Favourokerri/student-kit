from django.shortcuts import render
from notification.models import Notification, Welcome_Notification, General_Notification
from django.http import JsonResponse
import json

# Create your views here.

def notification(request):
    """ notification page"""
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')

    context = {
        "notifications": notifications
    }
    return render(request, 'dash_board/notification.html', context)

def mark_read(request):
    """makr notifications as read"""
    data = json.loads(request.body)
    question_id = data["id"]
    print(question_id)

  
    read_notification = Notification.objects.get(user=request.user, id=question_id)
    read_notification.read = True
    read_notification.save()
    return JsonResponse({"success": True})