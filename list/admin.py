from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task, Tag


# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     search_fields = ("model",)
#     list_filter = ("manufacturer",)

admin.site.register(Task)
admin.site.register(Tag)
from django.contrib import admin

# Register your models here.
