from datetime import datetime
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from admin.helper import superuser_only
from django.contrib.auth.decorators import login_required

from main.models import Booking, Yacht, YachtType, Package, Event, EventBooking, Training, TrainingBooking, Feedback, Employee

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


@login_required()
@superuser_only
def bookings_pdf(request):
    bookings = Booking.objects.all()

    pdf = render_to_pdf('pdfs/bookings/list.html', {'bookings': bookings, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Bookings.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response


@login_required()
@superuser_only
def booking_confirm(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    c_date = datetime.utcnow()

    pdf = render_to_pdf('pdfs/bookings/confirm.html', {'booking': booking, 'datetime': c_date})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = f"Booking_{booking_id}.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

# Yacht
@login_required()
@superuser_only
def yacht_type(request):
    yacht_types = YachtType.objects.all()

    pdf = render_to_pdf('pdfs/yacht_type.html', {'types': yacht_types, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Yacht_Types.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

@login_required()
@superuser_only
def yachts(request):
    yachts = Yacht.objects.all()

    pdf = render_to_pdf('pdfs/yachts.html', {'yachts': yachts, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Yachts.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

@login_required()
@superuser_only
def packages(request):
    packages = Package.objects.all()

    pdf = render_to_pdf('pdfs/packages.html', {'packages': packages, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Packages.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response


@login_required()
@superuser_only
def events(request):
    events = Event.objects.all()

    pdf = render_to_pdf('pdfs/events.html', {'events': events, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Events.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

@login_required()
@superuser_only
def event_bookings(request):
    event_bookings = EventBooking.objects.all()

    pdf = render_to_pdf('pdfs/events_booking.html', {'event_bookings': event_bookings, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Event_Bookings.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response


@login_required()
@superuser_only
def trainings(request):
    trainings = Training.objects.all()

    pdf = render_to_pdf('pdfs/trainings.html', {'trainings': trainings, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Trainings.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

@login_required()
@superuser_only
def training_bookings(request):
    training_bookings = TrainingBooking.objects.all()

    pdf = render_to_pdf('pdfs/training_booking.html', {'training_bookings': training_bookings, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Training_Bookings.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response


@login_required()
@superuser_only
def employees(request):
    emps = Employee.objects.all()

    pdf = render_to_pdf('pdfs/employees.html', {'emps': emps, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Employees.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

@login_required()
@superuser_only
def feedbacks(request):
    feedbacks = Feedback.objects.all()

    pdf = render_to_pdf('pdfs/feedbacks.html', {'feedbacks': feedbacks, 'datetime': datetime.utcnow()})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Feedbacks.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response