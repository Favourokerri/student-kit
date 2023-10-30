from django.contrib import admin
from .models import Welcome_Notification, Notification, General_Notification

class WelcomeNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'timestamp')
    ordering = ('-timestamp',)  # Order by timestamp in descending order

class GeneralNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'timestamp')
    ordering = ('-timestamp',)  # Order by timestamp in descending order

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'message', 'timestamp')
    ordering = ('-timestamp',)  # Order by timestamp in descending order

admin.site.register(Welcome_Notification, WelcomeNotificationAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(General_Notification, GeneralNotificationAdmin)