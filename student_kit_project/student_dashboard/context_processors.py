from notification.models import Notification

def unread_notification_count(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)
        unread_notification_count = sum(1 for notification in notifications if not notification.read)
        return {
            'unread_notification_count': unread_notification_count
        }
    return {'unread_notification_count': 0}