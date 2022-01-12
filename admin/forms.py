from django import forms
from main.models import Event, Training, YachtType, Yacht, Employee, Package


class YachtTypeForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = YachtType
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Yacht Type",
                }
            )
        }


class YachtForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = Yacht
        fields = ["name", "yacht_type", "capacity", "rate", "image"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Yacht Name",
                }
            ),
            "yacht_type": forms.Select(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Select Yacht Type",
                }
            ),
            "capacity": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Yacht Capacity",
                }
            ),
            "rate": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Yacht Rate",
                }
            )
        }

# Employee
class EmployeeForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = Employee
        exclude = ["created_at", "updated_at"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Last Name",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Email ID",
                }
            ),
            "mobile_number": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Mobile Number",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Enter Address",
                    "rows": 3
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Country",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Select Gender",
                }
            ),
            "designation": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Designation",
                }
            ),
            "yacht": forms.Select(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Select Yacht",
                }
            ),
        }


# Packages
class PackageForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = Package
        exclude = ["slug", "created_at", "updated_at"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Package Name",
                }
            ),
            "type": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Package Type",
                }
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Price",
                }
            ),
            "days": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Package days",
                }
            ),
            "persons": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Maximum Person Limit",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Enter Description",
                    "rows": 3
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block p-3 shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Activate Package",
                }
            ),
        }


# Event
class EventForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = Event
        exclude = ["slug", "created_at", "updated_at"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Event Name",
                }
            ),
            "type": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Event Type",
                }
            ),
            "days": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Event days",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Enter Description",
                    "rows": 3
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block p-3 shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Activate Event",
                }
            ),
        }


# Training
class TrainingForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = Training
        exclude = ["slug", "created_at", "updated_at"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Training Name",
                }
            ),
            "type": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Training Type",
                }
            ),
            "days": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Training days",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Enter Description",
                    "rows": 3
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block p-3 shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Activate Training",
                }
            ),
        }