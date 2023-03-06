from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import JobSeeker, Employer
from accounts.models import CustomUser

def home(request):
    return render(request,'home.html')

def job_seeker_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_job_seeker = True
            user.save()
            job_seeker = JobSeeker.objects.create(user=user)
            login(request, user)
            return redirect('job_seeker_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'job_seeker_register.html', {'form': form})

def employer_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employer = True
            user.save()
            employer = Employer.objects.create(user=user)
            login(request, user)
            return redirect('employer_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'employer_register.html', {'form': form})

def job_seeker_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_job_seeker:
            login(request, user)
            return redirect('job_seeker_dashboard')
        else:
            return render(request, 'job_seeker_login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'job_seeker_login.html')

def employer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_employer:
            login(request, user)
            return redirect('employer_dashboard')
        else:
            return render(request, 'employer_login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'employer_login.html')

@login_required
def job_seeker_logout(request):
    logout(request)
    return redirect('job_seeker_login')

@login_required
def employer_logout(request):
    logout(request)
    return redirect('employer_login')

@login_required
def job_seeker_dashboard(request):
    job_seeker = request.user.job_seeker
    # Add logic to retrieve job seeker's data and display it on the dashboard
    return render(request, 'job_seeker_dashboard.html', {'job_seeker': job_seeker})

@login_required
def employer_dashboard(request):
    employer = request.user.employer
    # Add logic to retrieve employer's data and display it on the dashboard
    return render(request, 'employer_dashboard.html', {'employer': employer})