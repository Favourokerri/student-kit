from django.test import TestCase
from django.contrib.auth.models import User
from flashcards.models import Card

class CardViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_add_card_view(self):
        self.client.login(username='testuser', password='testpassword')
        
        # Send a POST request to the add_card view
        response = self.client.post('/add_card/', {'title': 'Test Card', 'description': 'Test Description'})
        
        # Check if the card was added successfully
        self.assertEqual(response.status_code, 302)  # 302 is a redirect status code
        self.assertEqual(Card.objects.filter(user=self.user, title='Test Card').count(), 1)

    def test_cards_view(self):
        self.client.login(username='testuser', password='testpassword')
        
        # Send a GET request to the cards view
        response = self.client.get('/cards/')
        
        # Check if the response contains the expected data
        self.assertEqual(response.status_code, 200)  # 200 is a success status code
        self.assertContains(response, 'Test Card')  # Assuming you have a card with this title in the database

    def test_edith_card_view(self):
        self.client.login(username='testuser', password='testpassword')
        
        # Create a test card
        card = Card.objects.create(user=self.user, title='Test Card', description='Test Description')
        
        # Send a POST request to the edith_card view to edit the card
        response = self.client.post(f'/edith_card/{card.id}/', {'title': 'Updated Card', 'description': 'Updated Description'})
        
        # Check if the card was edited successfully
        self.assertEqual(response.status_code, 302)  # 302 is a redirect status code
        card.refresh_from_db()  # Refresh the card instance from the database
        self.assertEqual(card.title, 'Updated Card')
        
    def test_delete_card_view(self):
        self.client.login(username='testuser', password='testpassword')
        
        # Create a test card
        card = Card.objects.create(user=self.user, title='Test Card', description='Test Description')
        
        # Send a POST request to the delete_card view to delete the card
        response = self.client.post(f'/delete_card/{card.id}/')
        
        # Check if the card was deleted successfully
        self.assertEqual(response.status_code, 302)  # 302 is a redirect status code
        self.assertEqual(Card.objects.filter(user=self.user, title='Test Card').count(), 0)

