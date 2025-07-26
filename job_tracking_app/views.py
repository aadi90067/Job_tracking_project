from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import person
from .models import JobApplications
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        gmail = request.POST['email']
        passw = request.POST['password']

        if User.objects.filter(email=gmail).exists():
            messages.info(request, 'Email already exists')
            return redirect("register")
        else:
            user = User.objects.create_user(username=uname, email=gmail, password=passw)  # ✅ fixed method name & variable
            user.save()
            return redirect("login")
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']  # use username, not email
        passw = request.POST['password']

        user = auth.authenticate(request, username=uname, password=passw)  # ✅ fix here

        if user is not None:
            auth.login(request, user)
            return redirect('Dashboard')
        else:
            messages.info(request, 'Username and Password do not match')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required
def Dashboard(request):
    if request.method == "POST":
        job_title = request.POST['jobTitle']
        company = request.POST['company']
        application_date = request.POST['jobDate']
        status  = request.POST['status']

        JobApplications.objects.create(
            user=request.user,
            job_title=job_title,
            company=company,
            application_date=application_date,
            status=status
        )
        return redirect('Dashboard')
    else:
        jobs = JobApplications.objects.filter(user=request.user)
        return render(request, 'Dashboard.html', {'jobs': jobs})
    