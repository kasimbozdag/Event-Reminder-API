from rest_framework import serializers
from .models import Event, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'category', 'reminder_time']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_name = category_data.get('name')

        # Get or create the category
        category, created = Category.objects.get_or_create(name=category_name)

        # Create the event
        event = Event.objects.create(category=category, **validated_data)
        return event

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category_name = category_data.get('name')
            category, created = Category.objects.get_or_create(name=category_name)
            instance.category = category

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
