from django.contrib import admin
from abb.models import visitors
# Register your models here.

class visitorsadmin(admin.ModelAdmin):
    list_display=['name','mobile_no','feedback']
admin.site.register(visitors,visitorsadmin)