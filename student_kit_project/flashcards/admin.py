from django.contrib import admin
from .models import Card, Card_item

class CardsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'id')  # Customize the displayed fields in the list view

class CardItemAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'question')

    def get_user(self, obj):
        return obj.card.user

# Register the Cards model with the custom admin class
admin.site.register(Card, CardsAdmin)
admin.site.register(Card_item, CardItemAdmin)
