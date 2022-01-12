from django import forms
from .models import Feedback, Yacht


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


# Yacht Booking Form
class YachtBookingForm(forms.Form):
    template_name = "forms/template.html"

    yacht_id = forms.CharField(label=None, widget=forms.HiddenInput())
    from_date = forms.DateField(label="From Date", required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'}))
    to_date = forms.DateField(label="To Date", required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'}))
    persons = forms.IntegerField(label="Persons", required=True, widget=forms.NumberInput(attrs={'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md', 'placeholder': 'Enter Persons Count'}))

    def clean_persons(self):
        persons = self.cleaned_data.get("persons", "")
        yacht = Yacht.objects.filter(id=self.cleaned_data.get('yacht_id')).first()
        if yacht.capacity < persons:
            raise forms.ValidationError("Persons should not be greater than yacht capacity!")
        
        return persons


# Package Booking Form
class PackageBookingForm(forms.Form):
    template_name = "forms/template.html"

    package_id = forms.CharField(label=None, widget=forms.HiddenInput())
    from_date = forms.DateField(label="From Date", required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'}))


# Feedback
class FeedbackForm(forms.ModelForm):
    template_name = "forms/template.html"

    class Meta:
        model = Feedback
        exclude = ["created_at", "updated_at"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Name",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Email",
                }
            ),
            "mobile_number": forms.TextInput(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md",
                    "placeholder": "Enter Mobile Number",
                }
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md px-3 py-2",
                    "placeholder": "Enter Feedback",
                    "rows": 3
                }
            )
        }