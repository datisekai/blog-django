from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


def detail(request):
    return render(request, 'detail.html')


def login(request):
    return render(request, 'login.html')
