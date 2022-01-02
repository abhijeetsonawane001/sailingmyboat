from django.shortcuts import render, redirect
from .forms import LoginForm, CreateAccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Member, MemberManager


def index(request):
    return render(request, "index.html", {'title': 'Home'})

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

            # Check Member Exists or not
            member = Member.objects.filter(email=email).first()
            if member:
                messages.error(request, "Email already exists!")
                return redirect('main_create_account')
            
            member = Member.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)

            if member:
                login(request, member)
                return redirect('main_index')
            
    return render(request, "create_account.html", {'form': form, 'title': 'Create new Account'})
