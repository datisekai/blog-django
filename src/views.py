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
import uuid
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import get_connection
from django.core.mail.message import EmailMessage

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
                    break
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

            isUse = "isUseUsername"
            checkUser = User.objects.filter(username=username).first()
            checkEmail = User.objects.filter(email=email).first()
            if not checkUser:
                if not checkEmail:
                    isUse = "Success"
                else:
                    isUse = "isUseEmail"

            if isUse == "Success":
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


def ChangePasswordToken(request, token):
    return render(request, 'admin/change_password.html', {"tokenUser": token})


def ChangePassword(request, token):
    try:
        if request.method == "POST":
            raw_data = request.body
            data_string = raw_data.decode('utf-8')
            data = json.loads(data_string)

            password = data['password']
            isChangePassword = "Fail"
            users = User.objects.all()
            for item in users:
                if default_token_generator.check_token(item, token):
                    if str(password).find(str(item.username)) == -1:
                        isChangePassword = "Success"
                        item.set_password(password)
                        item.save()
                        user = authenticate(
                            request, username=item.username, password=password)
                        login(request, user)
                        break
                    else:
                        isChangePassword = "Similar"
                        break
            return JsonResponse({"isChangePassword": isChangePassword})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def forgetPassword(request):
    try:
        if request.method == "POST":
            raw_data = request.body
            data_string = raw_data.decode('utf-8')
            data = json.loads(data_string)

            username = data['username']

            isUser = False
            user = User.objects.filter(username=username).first()
            if user:
                token = default_token_generator.make_token(user)
                reset_url = f"{request.scheme}://{request.get_host()}/change_password/{token}/"
                email = user.email
                send_mail(
                    'Reset your password',
                    f'Please click the following link to reset your password: {reset_url}',
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                isUser = True
            return JsonResponse({"isUser": isUser})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def custom_login(request):
    return render(request, 'admin/custom_login.html')


def custom_register(request):
    return render(request, 'admin/custom_register.html')


def custom_forgetpassword(request):
    return render(request, 'admin/custom_forgetpassword.html')


def search(request):
    query = request.GET.get('q')
    return render(request, 'search.html', {"query": query})


def detail(request):
    return render(request, 'detail.html')


def getCategory(request):
    categories = Categories.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)
