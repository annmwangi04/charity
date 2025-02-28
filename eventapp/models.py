from django.db import models
from django.utils import timezone  

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='events/')
  
    date = models.DateTimeField(default=timezone.now)  
   
    def __str__(self):
        return self.name


class Booking(models.Model):
    cus_name = models.CharField(max_length=55)
    cus_ph = models.CharField(max_length=12)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now_add=True)