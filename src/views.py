from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
# Create your views here.


def home(request):
    user = request.user 
    return render(request, 'home.html', {'user': user})


def search(request):
    query = request.GET.get('q')
    return render(request, 'search.html',{"query":query})


def detail(request):
    return render(request, 'detail.html')


def login(request):
    return render(request, 'login.html')


def getCategory(request):
    categories = Categories.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)
