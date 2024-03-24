from django.shortcuts import render
from .models import Attendeesbooking
from rest_framework import generics
from .serializer import AttendeesSerializer
# Create your views here.

class AttendeesBook(generics.CreateAPIView):
    queryset=Attendeesbooking.objects.all()
    serializer_class=AttendeesSerializer

class AttendeesList(generics.ListAPIView):
    queryset = Attendeesbooking.objects.all()
    serializer_class=AttendeesSerializer
    
class AttendeesDelete(generics.RetrieveDestroyAPIView):
    queryset = Attendeesbooking.objects.all()
    serializer_class=AttendeesSerializer