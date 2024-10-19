# events/tests/test_serializers.py

from django.test import TestCase
from events.serializers import EventSerializer
from events.models import Event, Category
from datetime import date
from django.utils import timezone


class SerializerTests(TestCase):
    def test_event_serializer_with_valid_data(self):
        data = {
            'title': 'Team Meeting',
            'description': 'Monthly meeting',
            'date': str(date.today()),
            'time': '14:30',
            'category': {'name': 'Work'},
            'reminder_time': timezone.now()
        }
        serializer = EventSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        event = serializer.save()
        self.assertEqual(event.title, 'Team Meeting')
        self.assertEqual(event.category.name, 'Work')

    def test_event_serializer_with_invalid_time(self):
        data = {
            'title': 'Invalid Time Event',
            'description': 'Testing invalid time',
            'date': str(date.today()),
            'time': '25:00',  # Invalid time
            'category': {'name': 'Work'},
            'reminder_time': timezone.now()
        }
        serializer = EventSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('time', serializer.errors)
