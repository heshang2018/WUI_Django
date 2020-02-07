from django.contrib import admin

# Register your models here.

import hashlib

from django.contrib import admin
from .models import App



# admin.site.register(App)

@admin.register(App)
class APisAppAdmin(admin.ModelAdmin):

    fields = ['name','application','category','url','publish_date',
              'desc']

    pass

    def save_model(self, request, obj, form, change):
        src = obj.category + obj.application
        appid = hashlib.md5(src.encode('utf-8')).hexdigest()
        obj.appid = appid
        super().save_model(request,obj,form,change)