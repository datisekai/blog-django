from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def detail(request):
    return render(request, 'detail.html')


def login(request):
    return render(request, 'login.html')
