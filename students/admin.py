from django.contrib import admin

from .models import Student
from groups.models import Group


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['group']
    search_fields = ['number_card']

admin.site.register(Student, StudentAdmin)
