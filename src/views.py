from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.contrib.auth import logout
from .models import *
from django.db.models import Count
from django.http import JsonResponse
# Create your views here.


def home(request):
    user = request.user

    categories = Categories.objects.all()
    data = []
    for category in categories:
        blogs = category.blog_set.all()[:6]
        if blogs:
            data.append({
                'category': category,
                'blogs': blogs,
            })

    return render(request, 'home.html', {'user': user, "data_blogs": data, "first_category": data[0]})


def search(request):
    query = request.GET.get('q')
    return render(request, 'search.html', {"query": query})


def detail(request, slug):
    user = request.user
    obj = get_object_or_404(Blog, slug=slug)
    obj.html = format_html(obj.body)
    recommend_blogs = Blog.objects.filter(category=obj.category)[:6]
    context = {'data': obj, "recommend_blogs": recommend_blogs,"user":user}
    return render(request, 'detail.html', context)


def login(request):
    return render(request, 'login.html')


def getCategory(request):
    categories = Categories.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)


def logout_view(request):
    logout(request)
    return redirect('home')
