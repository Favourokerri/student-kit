from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
from django.contrib import messages
from flashcards.models import Card, Card_item
from .forms import ConfirmationForm
from django.forms.models import model_to_dict
# Create your views here.
def add_card(request):
    """ function for creating adds"""
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        card = Card.objects.create(user=request.user, title=title, description=description)
        card.save()
        messages.success(request, "   card has been added successfully")
        return redirect('cards')
    return render(request, 'flash_cards/add_card.html')

def cards(request):
    """ function to display cards"""
    cards = Card.objects.filter(user=request.user)

    context={"cards": cards}
    return render(request, 'flash_cards/cards.html', context)

def edith_card(request, card_id):
    """ function for edithing of cards"""
    card = Card.objects.get(user=request.user, id=card_id)
    if request.method == 'POST':
       title = request.POST['title']
       description = request.POST['description']
       
       card.title = title
       card.description = description
       card.save()
       messages.success(request, 'card edithed successfully')
       return redirect('cards')
    
    context = {"card": card}
    return render(request, 'flash_cards/edith_card.html', context )

def delete_card(request, card_id):
    """ function to delete cards """
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)
        card.delete()
        messages.success(request, "card deleted successfully")
        return redirect('cards')
    return render(request, 'flash_cards/confirm_delete.html')

def add_card_items(request, card_id):
    card = Card.objects.get(user=request.user, id=card_id)
    if request.method == 'POST':
        question = request.POST['question']
        action = request.POST.get('action') 

        try:
            card = Card.objects.get(user=request.user, id=card_id)
            card_item = Card_item.objects.create(card=card, question=question)
            card_item.save()
            if action == 'save':
                messages.success(request, 'card added successfully')
                return redirect('card_items', card_id=card_id)
            else:
                 messages.success(request, 'card added successfully add another')
        except Card.DoesNotExist:
            messages.error(request, 'Card not found')
    context = {"card": card}
    return render(request, 'flash_cards/add_card_items.html', context)

def card_items(request, card_id):
    card = Card.objects.get(id=card_id)
    card_items = Card_item.objects.filter(card__user=request.user, card__id=card_id)
    context = {
                "card_items": card_items,
                "card": card,
              }
    return render(request, 'flash_cards/card_items.html', context)

def edith_card_item(request, card_id):
    card = Card_item.objects.get(card__user=request.user, id=card_id)
    main_card = card.card #get main card so we can redirect back there

    if request.method == 'POST':
        question = request.POST['question']
        card.question = question
        card.save()
        messages.success(request, 'card edithed successfully')
        return redirect('card_items', card_id=main_card.id)
    context = {"card": card}
    return render(request, 'flash_cards/edith_card_item.html', context)

def delete_card_item(request, card_id):
    card = Card_item.objects.get(card__user=request.user, id=card_id)
    main_card = card.card #get main card so we can redirect back there

    if request.method == 'POST':
        card.delete()
        messages.success(request, 'card deleted successfully')
        return redirect('card_items', card_id=main_card.id)
    context={"card": card,
             "main_card": main_card}
    
    return render(request, 'flash_cards/confirm_delete2.html', context)

def text_to_speech(request):
    """ text to speach we send the card from the front 
        end to the backend unsing javascript and then we 
        grab the card id and send the title back to our js
        so we can convert to speech
    """
    data = json.loads(request.body)
    card_id = data['id']
    try:
        card = Card_item.objects.get(card__user=request.user, id=card_id)
    except Card_item.DoesNotExist:
        return JsonResponse({"error": "Card not found"}, status=404)
    
    card_data = model_to_dict(card)
    response_data = {
        "card": card_data,
        "question": card.question
    }
    return JsonResponse(response_data)