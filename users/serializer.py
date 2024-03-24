from rest_framework import serializers
from .models import Attendeesbooking

class AttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendeesbooking
        fields = ['name', 'email', 'phonenumber']