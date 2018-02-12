from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "home.html", {})
def login(request):
    return render(request, "login.html", {})

@login_required
def home(request):
    return render(request, "profile.html",{})
