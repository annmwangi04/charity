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

from django.db import models

class Cause(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def progress_percentage(self):
        if self.goal_amount == 0:
            return 0
        return int((self.current_amount / self.goal_amount) * 100)
    
    def __str__(self):
        return self.title

class SuccessStory(models.Model):
    title = models.CharField(max_length=200)
    completion_date = models.DateField()
    short_description = models.TextField()
    full_description = models.TextField()
    image = models.ImageField(upload_to='success_stories/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Success Stories"    