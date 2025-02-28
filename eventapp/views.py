from django.shortcuts import render, redirect
from .models import Event
from .forms import BookingForm
from django.contrib import messages
from django.utils import timezone  # Add this import for now()

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict__eve={
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
    return render(request, 'eventapp/events.html', {'upcoming_events': upcoming_events})