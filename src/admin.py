from django.contrib import admin
from .models import *
from django.db.models import Count



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


class Statisticals(admin.ModelAdmin):
    change_list_template = 'admin/statistical.html'

    def changelist_view(self, request, extra_context=None):

        user_count = User.objects.count()
        post_count = Blog.objects.count()
        category_count = Categories.objects.count()

        post_Statistical = Blog.objects.annotate(total_comments=Count('comments',distinct=True), total_reacts=Count('reacts',distinct=True)).all()

        context = {
            'user_count':user_count,
            'post_count':post_count,
            'category_count':category_count,
            'title':'Statistical',
            'post_Statistical':post_Statistical
        }

        return super().changelist_view(request, extra_context=context)
    
    def get_queryset(self, request):
        # Trả về một queryset trống để tắt tự động truy vấn của Django

        return Statistical.objects.none()


admin.site.register(Statistical,Statisticals)
admin.site.register(Categories)
admin.site.register(Blog,BlogAdmin)
# Register your models here.
