from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.contrib.auth import logout
from .models import *
from django.db.models import Count, Q
from django.http import JsonResponse
from django.core.paginator import Paginator
import math
from urllib.parse import parse_qsl, urlparse, urlencode
import json
from django.forms.models import model_to_dict

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
    results = []
    category = request.GET.get('category')
    if query:
        results = Blog.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
    elif category:
        results = Blog.objects.filter(Q(category__id__icontains=category))
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 6)

    paginator = Paginator(results, limit)
    data = paginator.get_page(page)
    current_url = request.build_absolute_uri()

    total_page = math.ceil(len(results)/int(limit))

    parsed_url = urlparse(current_url)
    query_next_page = dict(parse_qsl(parsed_url.query))
    next_page = None

    if int(page) < total_page:
        query_next_page['page'] = int(page) + 1

        next_page = urlencode(query_next_page)

    pre_page = None
    if int(page) > 1:

        query_pre_page = dict(parse_qsl(parsed_url.query))

        query_pre_page['page'] = int(page) - 1
        pre_page = urlencode(query_pre_page)

    context = {"query": query, "results": data, "total_page": total_page,
               "current_page": page, "limit": limit, "next_page": next_page, "pre_page": pre_page}
    print(context)
    return render(request, 'search.html', context)


def detail(request, slug):
    user = request.user
    obj = get_object_or_404(Blog, slug=slug)
    obj.html = format_html(obj.body)
    recommend_blogs = Blog.objects.filter(
        category=obj.category).exclude(id=obj.id)[:6]
    context = {'data': obj, "recommend_blogs": recommend_blogs, "user": user}
    return render(request, 'detail.html', context)


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

# API


def getCategory(request):
    categories = Categories.objects.all()
    data = list(categories.values())
    return JsonResponse(data, safe=False)


def getCommentAndReact(request, slug):
    obj = get_object_or_404(Blog, slug=slug)
    comments = Comments.objects.filter(
        blog=obj.id).select_related('author').order_by('-created_at')
    data_comments = []
    for comment in comments:
        data_comments.append({
            'id': comment.id,
            'content': comment.content,
            'author_id': comment.author_id,
            'author_username': comment.author.username,
            'author_email': comment.author.email,
            'created_at': comment.created_at,
        })
    reacts = Reacts.objects.filter(blog=obj.id)

    return JsonResponse({"comments": data_comments, "reacts": list(reacts.values())}, safe=False)


def addComment(request):
    try:
        if request.method == "POST":
            raw_data = request.body

            data_string = raw_data.decode('utf-8')

            data = json.loads(data_string)

            content = data['content']
            blog_id = data['blog_id']

            blog = get_object_or_404(Blog, id=int(blog_id))

            if content and blog_id:
                new_comment = Comments()
                new_comment.content = content
                new_comment.blog = blog
                new_comment.author = request.user
                new_comment.save()
                return JsonResponse({"comment": model_to_dict(new_comment), "current_username": request.user.username}, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def deleteComment(request, id):
    try:
        comment = get_object_or_404(Comments, id=id)
        if request.user == comment.author:
            comment.delete()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def updateComment(request, id):
    try:
        raw_data = request.body

        data_string = raw_data.decode('utf-8')

        data = json.loads(data_string)

        content = data['content']
        comment = get_object_or_404(Comments, id=id)

        if comment.author == request.user:
            comment.content = content
            comment.save()
            return JsonResponse({"comment": model_to_dict(comment),"current_username": request.user.username}, safe=False)
        return JsonResponse({"success": False, "message":"Not authorized", }, safe=False, status=401)
     
       

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def addLike(request,id):
    try:
        user = request.user
        current_blog = get_object_or_404(Blog, id=id)
        update = False
        delete = False
        try:
            is_exist = Reacts.objects.get(author=user, blog=current_blog)
        except Reacts.DoesNotExist:
            is_exist = None
        if is_exist:
            is_exist.delete()
            delete = True
        else:
            new_react = Reacts()
            new_react.author = user
            new_react.blog = current_blog
            new_react.icon = 'like'
            new_react.save()
            update = True
        return JsonResponse({"update":update, "delete":delete}, safe=False)    

    except Exception as e:
        return JsonResponse({"error":str(e)}, status=500)