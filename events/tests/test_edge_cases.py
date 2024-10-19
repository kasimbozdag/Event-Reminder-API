# events/tests/test_edge_cases.py

from rest_framework.test import APITestCase
from django.urls import reverse
from events.models import Event, Category
from django.utils import timezone
from datetime import time, date, timedelta
from rest_framework import status


class EdgeCaseTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Health')
        self.event = Event.objects.create(
            title='Past Event',
            description='An event in the past',
            date=date.today() - timedelta(days=2),
            time=time(10, 0),
            category=self.category,
            reminder_time=timezone.now() - timedelta(days=2)
        )
        self.event_list_url = reverse('event-list')
        self.upcoming_url = reverse('event-upcoming')

    def test_upcoming_events_with_no_events(self):
        response = self.client.get(self.upcoming_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_event_with_existing_category(self):
        url = self.event_list_url
        data = {
            'title': 'New Health Event',
            'description': 'Event with existing category',
            'date': str(date.today() + timedelta(days=1)),
            'time': '12:00',
            'category': {'name': 'Health'},
            'reminder_time': (timezone.now() + timedelta(hours=2)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.get(id=response.data['id']).category.name, 'Health')

    def test_create_event_without_category(self):
        url = self.event_list_url
        data = {
            'title': 'Event Without Category',
            'description': 'Should fail',
            'date': str(date.today()),
            'time': '10:00',
            # Missing 'category'
            'reminder_time': (timezone.now() + timedelta(hours=1)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('category', response.data)
