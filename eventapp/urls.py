from django.urls import path
from .views import index, contact, about, events, booking, event_list,news_updates,upcoming_events,success_stories,our_causes  

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('news-updates/',news_updates, name='news_updates'),
    path('upcoming-events/',upcoming_events, name='upcoming_events'),
    path('our-causes/',our_causes, name='our_causes'),
    path('success-stories/',success_stories, name='success_stories'),
    path('upcoming-events/', event_list, name='events-list'),  
]
