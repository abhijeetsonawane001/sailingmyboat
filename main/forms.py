from django import forms
from django.core.validators import EmailValidator


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
    