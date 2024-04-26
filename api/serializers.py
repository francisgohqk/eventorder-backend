from rest_framework import serializers

from .models import EventOrder


class EventOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventOrder
        fields = [
            'id',
            'title',
            'date',
            'start_time',
            'end_time',
            'sales',
            'attendance',
            'linen',
            'stage',
            'notes',
            'alcohol',
            'published_date',
        ]
