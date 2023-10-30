from django.contrib import admin
from .models import Room, Category, message

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'updated')
    list_filter = ('category',)  # Add any other filters you need
    search_fields = ('name',)  # Add any other search fields you want
    ordering = ('-updated',)  # This will order rooms by the 'updated' field in descending order

admin.site.register(Room, RoomAdmin)
admin.site.register(Category)
admin.site.register(message)