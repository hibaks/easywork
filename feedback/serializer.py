from rest_framework import serializers
from feedback.models import Feedback
from . models import Review
class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'

class android_serializer1(serializers.ModelSerializer):
    class Meta:

        model=Review
        fields='__all__'