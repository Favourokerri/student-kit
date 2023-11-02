from django.urls import path
from flashcards import views

urlpatterns = [
    path('add_card', views.add_card, name='add_card'),
    path('cards', views.cards, name='cards'),
    path('edith/<uuid:card_id>/', views.edith_card, name='edith_card'),
    path('delet/<uuid:card_id>/', views.delete_card, name="delete_card"),
    path('card_items/<uuid:card_id>/', views.card_items, name="card_items"),
    path('add_card_items/<uuid:card_id>/', views.add_card_items, name="add_card_items"),
    path('edith_card_item/<uuid:card_id>/', views.edith_card_item, name="edith_card_item"),
    path('delet_card_item/<uuid:card_id>/', views.delete_card_item, name="delete_card_item"),
    path('text_to_speech/', views.text_to_speech, name="text_to_speech"),
    path('practice/<uuid:card_id>/', views.practice, name="practice"),
]