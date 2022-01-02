from django import forms
from django.forms import fields
from django.forms.forms import Form
from main.models import YachtType, Yacht


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
            "yacht_type": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
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

# Yacht Form

