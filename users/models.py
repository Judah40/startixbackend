from django.db import models

# Create your models here.
class Attendeesbooking(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.IntegerField()

  
    
    class Meta:
        managed = False
        db_table = 'attendeesbooking'