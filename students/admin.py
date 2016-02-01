from django.contrib import admin

from .models import Student
from groups.models import Group

class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['group']
    search_fields = ['number_card']
    inlines = [GroupInline,]

admin.site.register(Student, StudentAdmin)
