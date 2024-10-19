# events/tests/test_custom_endpoints.py

from rest_framework.test import APITestCase
from django.urls import reverse
from events.models import Event, Category
from django.utils import timezone
from datetime import time, date, timedelta
from rest_framework import status


class CustomEndpointTests(APITestCase):
    def setUp(self):
        self.category_work = Category.objects.create(name='Work')
        self.category_personal = Category.objects.create(name='Personal')
        self.event_today = Event.objects.create(
            title='Event Today',
            description='Event happening today',
            date=date.today(),
            time=time(10, 0),
            category=self.category_work,
            reminder_time=timezone.now() + timedelta(hours=1)
        )
        self.event_tomorrow = Event.objects.create(
            title='Event After Tomorrow',
            description='Event happening After tomorrow',
            date=date.today() + timedelta(days=1),
            time=time(12, 0),
            category=self.category_personal,
            reminder_time=timezone.now() + timedelta(hours=25)
        )

    def test_get_upcoming_events(self):
        url = reverse('event-upcoming')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Event Today')

    def test_get_events_by_category(self):
        url = reverse('event-by-category', kwargs={'category_name': 'Personal'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category']['name'], 'Personal')
