from django.contrib import admin
from .models import *


class Statisticals(admin.ModelAdmin):
    change_list_template = "admin/statistical.html"

    def changelist_view(self, request, extra_context=None):
        context = {
            'title':''
        }
        return super().changelist_view(request, extra_context=context)


admin.site.register(Statistical,Statisticals)
admin.site.register(Categories)
admin.site.register(Blog)
# Register your models here.
