from django.shortcuts import render
from flashcards.models import Card
from chatRoom.models import Room 

def index(request):
    """Dashboard"""
    if request.user.is_authenticated:
        cards = Card.objects.filter(user=request.user)[:3]
        rooms = Room.objects.all()[:4]
        context = {
                   "cards": cards,
                   "rooms": rooms}
        return render(request, 'dash_board/dash_board.html', context)
    else:
        return render(request, 'landing_page/signup.html')