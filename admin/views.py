from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from main.models import (
    Employee,
    Event,
    EventBooking,
    Package,
    Training,
    TrainingBooking,
    Yacht,
    YachtType,
)

from .forms import (
    EventForm,
    TrainingForm,
    YachtTypeForm,
    YachtForm,
    EmployeeForm,
    PackageForm,
)
from .helper import superuser_only


@login_required()
@superuser_only
def dashboard(request):
    return render(request, "admin/base.html", {"title": "Dashboard"})


# YACHT TYPES
@login_required()
@superuser_only
def yacht_type_list(request):
    yacht_types = YachtType.objects.all()
    context = {"title": "Yacht Types", "yacht_types": yacht_types}
    return render(request, "admin/yachts/yacht_type_list.html", context=context)


@login_required()
@superuser_only
def yacht_type_add(request):
    form = YachtTypeForm()
    if request.method == "POST":
        form = YachtTypeForm(request.POST)
        if form.is_valid():
            yacht_type = YachtType.objects.filter(
                slug=slugify(form.cleaned_data.get("name"))
            ).first()
            if yacht_type:
                messages.error(request, "Yacht Type slug already exists!")
                return redirect("admin_yacht_type_add")
            form.save()
            return redirect("admin_yacht_type_list")

    return render(
        request,
        "admin/yachts/yacht_type_add.html",
        {"form": form, "title": "Add Yacht Type"},
    )


@login_required()
@superuser_only
def yacht_type_edit(request, slug):
    yacht_type = YachtType.objects.filter(slug=slug).first()

    if not yacht_type:
        messages.error(request, "No Yacht Type found!")
        return redirect("admin_yacht_type_list")

    form = YachtTypeForm(instance=yacht_type)

    if request.method == "POST":
        form = YachtTypeForm(request.POST, instance=yacht_type)
        if form.is_valid():
            form.save()
            return redirect("admin_yacht_type_list")
    return render(
        request,
        "admin/yachts/yacht_type_edit.html",
        {"form": form, "title": "Edit Yacht Type"},
    )


@login_required()
@superuser_only
def yacht_type_delete(request, slug):
    yacht_type = YachtType.objects.filter(slug=slug).delete()

    return redirect("admin_yacht_type_list")


# YACHT
@login_required()
@superuser_only
def yacht_list(request):
    yachts = Yacht.objects.all()
    return render(
        request, "admin/yachts/yacht_list.html", {"title": "Yachts", "yachts": yachts}
    )


@login_required()
@superuser_only
def yacht_add(request):
    form = YachtForm()
    if request.method == "POST":
        form = YachtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_yacht_list")
        else:
            messages.error(request, "Error while adding Yacht!")
            return redirect("admin_yacht_add")
    return render(
        request, "admin/yachts/yacht_add.html", {"title": "Add Yacht", "form": form}
    )


@login_required()
@superuser_only
def yacht_edit(request, pk):
    yacht = Yacht.objects.filter(id=pk).first()
    if not yacht:
        messages.error(request, "No Yacht found!")
        return redirect("admin_yacht_list")

    form = YachtForm(instance=yacht)

    if request.method == "POST":
        form = YachtForm(request.POST, request.FILES, instance=yacht)
        if form.is_valid():
            form.save()
            return redirect("admin_yacht_list")
    return render(
        request,
        "admin/yachts/yacht_edit.html",
        {"form": form, "title": "Edit Yacht"},
    )


@login_required()
@superuser_only
def yacht_delete(request, pk):
    yacht = Yacht.objects.filter(id=pk).delete()

    return redirect("admin_yacht_list")


# Employees
def employee_list(request):
    employees = Employee.objects.all()

    context = {"title": "Employees", "employees": employees}
    return render(request, "admin/employees/list.html", context)


@login_required()
@superuser_only
def employee_add(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_employee_list")
        else:
            messages.error(request, "Error while adding Employee!")
            return redirect("admin_employee_add")

    context = {"title": "Add Employee", "form": form}
    return render(request, "admin/employees/add.html", context)


@login_required()
@superuser_only
def employee_edit(request, email):
    emp = Employee.objects.filter(email=email).first()
    if not emp:
        messages.error(request, "No Employee found!")
        return redirect("admin_employee_list")

    form = EmployeeForm(instance=emp)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect("admin_employee_list")

    context = {"form": form, "title": "Edit Employee"}
    return render(request, "admin/employees/edit.html", context)


@login_required()
@superuser_only
def employee_delete(request, email):
    emp = Employee.objects.filter(email=email).delete()

    return redirect("admin_employee_list")


# Packages
@login_required()
@superuser_only
def package_list(request):
    packages = Package.objects.all()
    return render(
        request,
        "admin/packages/package_list.html",
        {"title": "Packages", "packages": packages},
    )


@login_required()
@superuser_only
def package_add(request):
    form = PackageForm()
    if request.method == "POST":
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_package_list")
        else:
            messages.error(request, "Error while adding Package!")
            return redirect("admin_package_add")
    return render(
        request,
        "admin/packages/package_add.html",
        {"title": "Add Package", "form": form},
    )


@login_required()
@superuser_only
def package_edit(request, pk):
    package = Package.objects.filter(id=pk).first()
    if not package:
        messages.error(request, "No Package found!")
        return redirect("admin_package_list")

    form = PackageForm(instance=package)

    if request.method == "POST":
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect("admin_package_list")
    return render(
        request,
        "admin/packages/package_edit.html",
        {"form": form, "title": "Edit Package"},
    )


@login_required()
@superuser_only
def package_delete(request, pk):
    package = Package.objects.filter(id=pk).delete()

    return redirect("admin_package_list")


# Events
@login_required()
@superuser_only
def event_list(request):
    events = Event.objects.all()
    return render(
        request, "admin/events/event_list.html", {"title": "Events", "events": events}
    )


@login_required()
@superuser_only
def event_add(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_event_list")
        else:
            messages.error(request, "Error while adding Event!")
            return redirect("admin_event_add")
    return render(
        request, "admin/events/event_add.html", {"title": "Add Event", "form": form}
    )


@login_required()
@superuser_only
def event_edit(request, pk):
    event = Event.objects.filter(id=pk).first()
    if not event:
        messages.error(request, "No Event found!")
        return redirect("admin_event_list")

    form = EventForm(instance=event)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("admin_event_list")
    return render(
        request,
        "admin/events/event_edit.html",
        {"form": form, "title": "Edit Event"},
    )


@login_required()
@superuser_only
def event_delete(request, pk):
    event = Event.objects.filter(id=pk).delete()

    return redirect("admin_event_list")


@login_required()
@superuser_only
def event_booking(request):
    event_bookings = EventBooking.objects.all()
    context = {"title": "Event Registrations", "bookings": event_bookings}
    return render(request, "admin/events/bookings_list.html", context)



# Trainings
@login_required()
@superuser_only
def training_list(request):
    trainings = Training.objects.all()
    return render(
        request,
        "admin/trainings/training_list.html",
        {"title": "Trainings", "trainings": trainings},
    )


@login_required()
@superuser_only
def training_add(request):
    form = TrainingForm()
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_training_list")
        else:
            messages.error(request, "Error while adding Training!")
            return redirect("admin_training_add")
    return render(
        request,
        "admin/trainings/training_add.html",
        {"title": "Add Training", "form": form},
    )


@login_required()
@superuser_only
def training_edit(request, pk):
    training = Training.objects.filter(id=pk).first()
    if not training:
        messages.error(request, "No Training found!")
        return redirect("admin_training_list")

    form = TrainingForm(instance=training)

    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect("admin_training_list")
    return render(
        request,
        "admin/trainings/training_edit.html",
        {"form": form, "title": "Edit Training"},
    )


@login_required()
@superuser_only
def training_delete(request, pk):
    training = Training.objects.filter(id=pk).delete()

    return redirect("admin_training_list")

@login_required()
@superuser_only
def training_booking(request):
    training_bookings = TrainingBooking.objects.all()
    context = {"title": "Training Registrations", "bookings": training_bookings}
    return render(request, "admin/trainings/bookings_list.html", context)