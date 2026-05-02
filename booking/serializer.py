from rest_framework import serializers
from booking.models import Book
class android_serializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    worker = serializers.CharField(source='service.worker.name', read_only=True)

    class Meta:
        model = Book
        # fields = '__all__'
        fields = [
            'book_id',
            'worker',
            'service_name',
            'date',
            'time',
            'status'
        ]