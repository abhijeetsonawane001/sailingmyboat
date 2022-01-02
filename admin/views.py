from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from main.models import Yacht, YachtType

from .forms import YachtTypeForm
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
def yacht_list(request):
    pass

def yacht_add(request):
    pass
