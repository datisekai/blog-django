from django.contrib import admin
from .models import *


class Statisticals(admin.ModelAdmin):
    change_list_template = "admin/statistical.html"

    def changelist_view(self, request, extra_context=None):
        context = {
            'title':''
        }
        return super().changelist_view(request, extra_context=context)


class BlogAdmin(admin.ModelAdmin):
    exclude = ['author']
    def get_queryset(self, request):
        # Lọc danh sách các blog theo người dùng đăng nhập và quyền "view_my_posts"
        qs = super().get_queryset(request)
        user = request.user
        if user.has_perm('src.view_my_posts'):
            return qs.filter(author=user)
        else:
            return qs
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Statistical,Statisticals)
admin.site.register(Categories)
admin.site.register(Blog,BlogAdmin)
# Register your models here.
