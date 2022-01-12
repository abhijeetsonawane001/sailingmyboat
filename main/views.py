from django.shortcuts import render, redirect
from .forms import (
    EventBookingForm,
    FeedbackForm,
    LoginForm,
    CreateAccountForm,
    PackageBookingForm,
    TrainingBookingForm,
    YachtBookingForm,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    Booking,
    Event,
    EventBooking,
    Member,
    Package,
    Payment,
    Training,
    TrainingBooking,
    Yacht,
)
from datetime import timedelta, datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from core.settings import RAZORPAY_ID, RAZORPAY_SECRET
import razorpay

rp_client = razorpay.Client(auth=(RAZORPAY_ID, RAZORPAY_SECRET))


def index(request):
    yachts = Yacht.objects.all()

    context = {"title": "Book Yachts", "yachts": yachts}
    return render(request, "index.html", context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # authenticate user
            member = authenticate(request, username=email, password=password)
            if member is not None:
                login(request, member)
                if member.is_superuser:

                    return redirect(request.GET.get("next", "admin_dashboard"))
                else:
                    return redirect(request.GET.get("next", "main_index"))
            else:
                messages.error(request, "Invalid Credentials")
                return redirect("main_login")
    return render(request, "login.html", {"form": form, "title": "Login"})


def logout_view(request):
    logout(request)
    return redirect("main_index")


def create_account(request):
    form = CreateAccountForm()
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            mobile_number = form.cleaned_data["mobile_number"]
            address = form.cleaned_data["address"]
            country = form.cleaned_data["country"]
            gender = form.cleaned_data["gender"]

            # Check Member Exists or not
            member = Member.objects.filter(email=email).first()
            if member:
                messages.error(request, "Email already exists!")
                return redirect("main_create_account")

            member = Member.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                mobile_number=mobile_number,
                address=address,
                country=country,
                gender=gender,
            )

            if member:
                login(request, member)
                return redirect("main_index")

    return render(
        request, "create_account.html", {"form": form, "title": "Create new Account"}
    )


# Yacht Detail
def yacht_detail(request, pk):
    yacht = Yacht.objects.filter(id=pk).first()
    form = YachtBookingForm()
    form.initial["yacht_id"] = yacht.id

    if request.method == "POST":
        form = YachtBookingForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data.get("from_date")
            to_date = form.cleaned_data.get("to_date")
            persons = form.cleaned_data.get("persons")

            date_diff = to_date - from_date
            days = date_diff.days
            if days == 0:
                days = 1

            amount = days * yacht.rate
            request.session["current_booking"] = json.dumps(
                {
                    "from_date": from_date,
                    "to_date": to_date,
                    "yacht": {
                        "name": yacht.name,
                        "persons": persons,
                        "amount": amount,
                        "id": yacht.id,
                        "days": days,
                        "price": yacht.rate,
                    },
                },
                cls=DjangoJSONEncoder,
            )

            return redirect("main_booking")

    context = {"title": f"{yacht.name} Details", "yacht": yacht, "form": form}
    return render(request, "yacht_detail.html", context)


# Events
def events_list(request):
    events = Event.objects.filter(is_active=True).all()

    context = {"title": "Events", "events": events}
    return render(request, "events/index.html", context)


def events_detail(request, pk):
    event = Event.objects.filter(id=pk).first()

    context = {"title": "Event Information", "event": event}

    return render(request, "events/detail.html", context)


@login_required()
def event_booking(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    if not event:
        return redirect("main_event_list")
    form = EventBookingForm()

    if request.method == "POST":
        form = EventBookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["event_date"]
            end_date = start_date + timedelta(days=event.days)

            event_booking = EventBooking(
                event=event,
                member=request.user,
                start_date=start_date,
                end_date=end_date,
            )

            event_booking.save()

            # Show successful page and generate PDF
            return redirect("main_event_list")
    return render(
        request,
        "events/register.html",
        context={"title": "Event Registration", "form": form},
    )


# Trainings
def trainings_list(request):
    trainings = Training.objects.filter(is_active=True).all()

    context = {"title": "Trainings", "trainings": trainings}
    return render(request, "trainings/index.html", context)


def trainings_detail(request, pk):
    training = Training.objects.filter(id=pk).first()

    context = {"title": "Training Information", "training": training}

    return render(request, "trainings/detail.html", context)


@login_required()
def training_booking(request, training_id):
    training = Training.objects.filter(id=training_id).first()
    if not training:
        return redirect("main_training_list")
    form = TrainingBookingForm()

    if request.method == "POST":
        form = TrainingBookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["training_date"]
            end_date = start_date + timedelta(days=training.days)

            training_booking = TrainingBooking(
                training=training,
                member=request.user,
                start_date=start_date,
                end_date=end_date,
            )

            training_booking.save()

            # Show successful page and generate PDF
            return redirect("main_training_list")
    return render(
        request,
        "trainings/register.html",
        context={"title": "Training Registration", "form": form},
    )


# Packages
def package_list(request):
    packages = Package.objects.filter(is_active=True).all()

    context = {"title": "Packages", "packages": packages}
    return render(request, "packages/index.html", context)


def package_detail(request, pk):
    package = Package.objects.filter(id=pk).first()
    form = PackageBookingForm()
    form.initial["package_id"] = package.id

    if request.method == "POST":
        form = PackageBookingForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data.get("from_date")
            to_date = from_date + timedelta(days=package.days)

            request.session["current_booking"] = json.dumps(
                {
                    "from_date": from_date,
                    "to_date": to_date,
                    "package": {
                        "name": package.name,
                        "persons": package.persons,
                        "amount": package.price,
                        "id": package.id,
                        "days": package.days,
                        "price": package.price,
                    },
                },
                cls=DjangoJSONEncoder,
            )
            return redirect("main_booking")

    context = {"title": "Package Information", "package": package, "form": form}
    return render(request, "packages/detail.html", context)


# Commom Booking Page For YACHT & PACKAGE
@login_required()
def booking(request):
    if not request.session.get("current_booking"):
        return redirect("main_index")

    booking_order = json.loads(request.session.get("current_booking"))
    booking_order["from_date"] = datetime.strptime(
        booking_order["from_date"], "%Y-%m-%d"
    )
    booking_order["to_date"] = datetime.strptime(booking_order["to_date"], "%Y-%m-%d")

    amount = 0
    amount_in_ps = 0
    # If Yacht get yacht information
    yacht_obj = None
    package_obj = None
    persons = 0
    if booking_order.get("yacht"):
        amount = booking_order["yacht"]["amount"]
        amount_in_ps = amount * 100
    # If package get package information
    if booking_order.get("package"):
        amount = booking_order["package"]["amount"]
        amount_in_ps = amount * 100

    # Create order
    DATA = {
        "amount": amount_in_ps,
        "currency": "INR",
        "notes": {
            "booking": f"Booking for {request.user.email}"
        }
    }
    payment_order = rp_client.order.create(data=DATA)
    # Store all detail in new session obj
    
    # After successful payment Create Booking and Payment records

    context = {
        "title": "Booking Confirmation",
        "booking": booking_order,
        "payment_info": {
            "amount_in_ps": amount_in_ps,
            "key_id": RAZORPAY_ID,
            "prefill": {
                "name": f"{request.user.first_name} {request.user.last_name}",
                "email": request.user.email,
                "contact": request.user.mobile_number,
            },
            "order_id": payment_order['id']
        },
    }
    return render(request, "booking.html", context)


def success(request):
    if not request.GET.get('payment_id') or not request.GET.get('order_id'):
        request.session.pop('current_booking')

        return redirect("main_index")

    if not request.session.get("current_booking"):
        return redirect("main_index")
    booking_order = json.loads(request.session.get("current_booking"))

    payment_id = request.GET.get('payment_id')
    order_id = request.GET.get('order_id')

    # If Yacht get yacht information
    yacht_obj = None
    package_obj = None
    persons = 0
    amount = 0
    if booking_order.get("yacht"):
        yacht_obj = Yacht.objects.get(id=booking_order["yacht"]["id"])
        amount = booking_order["yacht"]["amount"]
        persons = booking_order['yacht']['persons']
    # If package get package information
    if booking_order.get("package"):
        package_obj = Package.objects.get(id=booking_order["package"]["id"])
        amount = booking_order["package"]["amount"]
        persons = booking_order['package']['persons']


    booking = Booking(
        persons=persons,
        start_date=booking_order["from_date"],
        end_date=booking_order["to_date"],
        amount=amount,
        member=request.user,
        yacht=yacht_obj,
        package=package_obj,
        status="success"
    )
    booking.save()

    payment = Payment(booking=booking, payment_id=payment_id, order_id=order_id, status="success")
    payment.save()

    request.session.pop('current_booking')
    return render(request, 'success.html')


# Feedback
def feedback(request):
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback submitted successfully!")
            return redirect('main_feedback')
    
    return render(request, 'feedback.html', {'title': 'Feedback', 'form': form})