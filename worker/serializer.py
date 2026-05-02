from rest_framework import serializers
from worker.models import Worker

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields='__all__'