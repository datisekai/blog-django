from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import *
from .models import *
from django.http import JsonResponse
import logging
import traceback
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import check_password
# Create your views here.


def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})


def isLogin(request):
    try:
        if request.method == "POST":
            raw_data = request.body
            data_string = raw_data.decode('utf-8')
            data = json.loads(data_string)

            username = data['username']
            password = data['password']
            isLogin = False

            users = User.objects.all()
            for item in users:
                if item.username == username and check_password(password, item.password):
                    isLogin = True
                    user = authenticate(
                        request, username=username, password=password)
                    login(request, user)
        return JsonResponse({"isLogin": isLogin})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def isResister(request):
    try:
        if request.method == "POST":
            raw_data = request.body
            data_string = raw_data.decode('utf-8')
            data = json.loads(data_string)

            username = data['username']
            password = data['password']
            hashed_password = make_password(password)
            email = data['email']

            users = User.objects.all()
            isUse = False
            for item in users:
                if item.username == username:
                    isUse = True

            if isUse == False:
                user = User.objects.create(
                    username=username, password=hashed_password, email=email, is_staff=True)
                group = Group.objects.get(name='User')
                user.groups.add(group)
                user = authenticate(
                    request, username=username, password=password)
                login(request, user)
        return JsonResponse({"isUse": isUse})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def custom_login(request):
    users = User.objects.all()
    return render(request, 'admin/custom_login.html', {"user": users})


def custom_register(request):
    users = User.objects.all()
    return render(request, 'admin/custom_register.html', {"user": users})


def search(request):
    query = request.GET.get('q')
    return render(request, 'search.html', {"query": query})


def detail(request):
    return render(request, 'detail.html')


def getCategory(request):
    categories = Categories.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)
