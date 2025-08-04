from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserLoginForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f'/{user.role.lower()}_dashboard/')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(username=identifier).first() or \
                   CustomUser.objects.filter(email=identifier).first()
            if user:
                user = authenticate(username=user.username, password=password)
                if user:
                    login(request, user)
                    return redirect(f'/{user.role.lower()}_dashboard/')
            error = "Invalid credentials"
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})
