from django import forms
from django.core.validators import EmailValidator
from .models import EventBooking, Member


class LoginForm(forms.Form):
    template_name = "forms/template.html"

    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Email address'}))
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Password'})
    )


class CreateAccountForm(forms.Form):
    template_name = "forms/template.html"

    first_name = forms.CharField(label="First Name", required=True, widget=forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Email address'}))
    last_name = forms.CharField(label="Last Name", required=True, widget=forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Email address'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Email address'}))
    password = forms.CharField(
        label="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Password'})
    )
    mobile_number = forms.CharField(label="Mobile Number", required=True, widget=forms.NumberInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Mobile Number'}))
    address = forms.CharField(label="Address", required=True, widget=forms.Textarea(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2', 'placeholder': 'Enter Address', 'rows': '3'}))
    country = forms.CharField(label="Country", required=True, widget=forms.TextInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Country'}))
    gender = forms.CharField(label="Gender", required=True, widget=forms.Select(choices=(('M', 'Male'), ('F', 'Female')), attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2', 'placeholder': 'Select Gender'}))


# Event Booking Form
class EventBookingForm(forms.Form):
    template_name = "forms/template.html"
    
    event_date = forms.DateField(label="Select Event Date", required=True, widget=forms.DateInput(attrs={'type': 'date'}))

# Training Booking Form
class TrainingBookingForm(forms.Form):
    template_name = "forms/template.html"
    
    training_date = forms.DateField(label="Select Training Date", required=True, widget=forms.DateInput(attrs={'type': 'date'}))
