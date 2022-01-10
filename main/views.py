from django.shortcuts import render, redirect
from .forms import EventBookingForm, LoginForm, CreateAccountForm, TrainingBookingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventBooking, Member, Training, TrainingBooking, Yacht
from datetime import timedelta


def index(request):
    yachts = Yacht.objects.all()

    context = {'title': 'Book Yachts', 'yachts': yachts}
    return render(request, "index.html", context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # authenticate user
            member = authenticate(request, username=email, password=password)
            if member is not None:
                login(request, member)
                if member.is_superuser:
                    
                    return redirect(request.GET.get('next', 'admin_dashboard'))
                else:
                    return redirect(request.GET.get('next', 'main_index'))
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('main_login')
    return render(request, "login.html", {'form': form, 'title': 'Login'})


def logout_view(request):
    logout(request)
    return redirect('main_index')

def create_account(request):
    form = CreateAccountForm()
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            mobile_number = form.cleaned_data['mobile_number']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            gender = form.cleaned_data['gender']

            # Check Member Exists or not
            member = Member.objects.filter(email=email).first()
            if member:
                messages.error(request, "Email already exists!")
                return redirect('main_create_account')
            
            member = Member.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, mobile_number=mobile_number, address=address, country=country, gender=gender)

            if member:
                login(request, member)
                return redirect('main_index')
            
    return render(request, "create_account.html", {'form': form, 'title': 'Create new Account'})


# Yacht Detail
def yacht_detail(request, pk):
    yacht = Yacht.objects.filter(id=pk).first()

    context = {'title': f"{yacht.name} Details", 'yacht': yacht}
    return render(request, 'yacht_detail.html', context)


# Events
def events_list(request):
    events = Event.objects.filter(is_active=True).all()

    context = {'title': "Events", 'events': events}
    return render(request, 'events/index.html', context)


def events_detail(request, pk):
    event = Event.objects.filter(id=pk).first()

    context = {'title': 'Event Information', 'event': event}

    return render(request, 'events/detail.html', context)
    

@login_required()
def event_booking(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    if not event:
        return redirect('main_event_list')
    form = EventBookingForm()

    if request.method == "POST":
        form = EventBookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['event_date']
            end_date = start_date+timedelta(days=event.days)

            event_booking = EventBooking(event=event, member=request.user, start_date=start_date, end_date=end_date)

            event_booking.save()

            # Show successful page and generate PDF
            return redirect('main_event_list')
    return render(request, 'events/register.html', context={'title': 'Event Registration', 'form':form})


# Trainings
def trainings_list(request):
    trainings = Training.objects.filter(is_active=True).all()

    context = {'title': "Trainings", 'trainings': trainings}
    return render(request, 'trainings/index.html', context)


def trainings_detail(request, pk):
    training = Training.objects.filter(id=pk).first()

    context = {'title': 'Training Information', 'training': training}

    return render(request, 'trainings/detail.html', context)
    

@login_required()
def training_booking(request, training_id):
    training = Training.objects.filter(id=training_id).first()
    if not training:
        return redirect('main_training_list')
    form = TrainingBookingForm()

    if request.method == "POST":
        form = TrainingBookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['training_date']
            end_date = start_date+timedelta(days=training.days)

            training_booking = TrainingBooking(training=training, member=request.user, start_date=start_date, end_date=end_date)

            training_booking.save()

            # Show successful page and generate PDF
            return redirect('main_training_list')
    return render(request, 'trainings/register.html', context={'title': 'Training Registration', 'form':form})
