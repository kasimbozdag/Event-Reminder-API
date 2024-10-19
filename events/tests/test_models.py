# events/tests/test_models.py

from django.test import TestCase
from events.models import Event, Category
from django.utils import timezone
from datetime import time, date, timedelta


class ModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Work')
        self.event = Event.objects.create(
            title='Meeting',
            description='Team meeting',
            date=date.today(),
            time=time(14, 30),
            category=self.category,
            reminder_time=timezone.now() + timedelta(hours=1)
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Work')
        self.assertIsInstance(self.category, Category)

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Meeting')
        self.assertEqual(self.event.category.name, 'Work')
        self.assertIsInstance(self.event, Event)
