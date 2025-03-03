from django.contrib import admin
from .models import Event,Booking,Cause, SuccessStory

# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Cause)
admin.site.register(SuccessStory)


