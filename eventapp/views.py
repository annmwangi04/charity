from django.shortcuts import render, redirect
from .models import Event, Cause, SuccessStory  # Import all models at the top
from .forms import BookingForm
from django.contrib import messages
from django.utils import timezone
import requests
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict__eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict__eve)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookingForm()
    dict_form = {'form': form}
    return render(request, 'booking.html', dict_form)

def contact(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        messages.success(request, "Thank you for your message! We'll get back to you soon.")
        return redirect('contact')
    return render(request, 'contact.html')

def event_list(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')[:5]  
    return render(request, 'events.html', {'upcoming_events': upcoming_events})

def news_updates(request):
    # Here you would typically fetch news/updates from your database
    # For now, we'll just render a template
    return render(request, 'news_updates.html')

def upcoming_events(request):
    # Example using Eventbrite API
    try:
        # You would need to get an API key from Eventbrite
        api_key = settings.EVENTBRITE_API_KEY
        url = "https://www.eventbriteapi.com/v3/events/search/"
        
        # Parameters to find charity events
        params = {
            'q': 'charity',
            'sort_by': 'date',
            'categories': '111',  # This is Eventbrite's category ID for charity & causes
            'location.address': 'United States',  # You can change this to any location
        }
        
        headers = {
            'Authorization': f'Bearer {api_key}',
        }
        
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        
        events = data.get('events', [])
        return render(request, 'upcoming_events.html', {'events': events})
    
    except Exception as e:
        # If API call fails, display empty page with error message
        return render(request, 'upcoming_events.html', {
            'events': [],
            'error_message': f"Could not fetch events: {str(e)}"
        })

def our_causes(request):
    causes = Cause.objects.all().order_by('-created_at')
    return render(request, 'our_causes.html', {'causes': causes})

def success_stories(request):
    stories = SuccessStory.objects.all().order_by('-completion_date')
    return render(request, 'success_stories.html', {'stories': stories})