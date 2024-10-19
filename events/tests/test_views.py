# events/tests/test_views.py

from rest_framework.test import APITestCase
from django.urls import reverse
from events.models import Event, Category
from django.utils import timezone
from datetime import time, date, timedelta
from rest_framework import status


class APITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Work')
        self.event = Event.objects.create(
            title='Existing Event',
            description='An existing event',
            date=date.today(),
            time=time(10, 0),
            category=self.category,
            reminder_time=timezone.now() + timedelta(hours=1)
        )
        self.event_url = reverse('event-detail', kwargs={'pk': self.event.id})
        self.event_list_url = reverse('event-list')

    def test_create_event(self):
        url = self.event_list_url
        data = {
            'title': 'New Event',
            'description': 'Creating a new event',
            'date': str(date.today() + timedelta(days=1)),
            'time': '15:00',
            'category': {'name': 'Personal'},
            'reminder_time': (timezone.now() + timedelta(hours=2)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.get(id=response.data['id']).title, 'New Event')

    def test_retrieve_event_list(self):
        url = self.event_list_url
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_event_detail(self):
        url = self.event_url
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Existing Event')

    def test_update_event(self):
        url = self.event_url
        data = {
            'title': 'Updated Event',
            'description': 'An updated event',
            'date': str(date.today()),
            'time': '11:00',
            'category': {'name': 'Work'},
            'reminder_time': (timezone.now() + timedelta(hours=1)).isoformat()
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, 'Updated Event')
        self.assertEqual(self.event.time, time(11, 0))

    def test_delete_event(self):
        url = self.event_url
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)
