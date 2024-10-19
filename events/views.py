from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import action
import logging

from django.db.models import ExpressionWrapper, F, DateTimeField, Value as V, CharField
from django.db.models.functions import Concat, Cast

logger = logging.getLogger(__name__)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating a new event with data: {request.data}")
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        now = timezone.now()
        next_24_hours = now + timedelta(hours=24)
            # Combine 'date' and 'time' into a datetime string
        events = Event.objects.annotate(
            event_datetime=ExpressionWrapper(
                Cast(
                    Concat(
                        F('date'),
                        V(' '),
                        F('time'),
                        output_field=CharField()
                    ),
                    output_field=DateTimeField()
                ),
                output_field=DateTimeField()
            )
        ).filter(
            event_datetime__gte=now,
            event_datetime__lte=next_24_hours
        )
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='category/(?P<category_name>[^/.]+)')
    def by_category(self, request, category_name=None):
        events = Event.objects.filter(category__name=category_name)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
