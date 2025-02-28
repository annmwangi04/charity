from django.urls import path
from .views import index, contact, about, events, booking, event_list  

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('upcoming-events/', event_list, name='events-list'),  
]
