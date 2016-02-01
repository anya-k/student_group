from django.contrib import admin

from .models import Student, Group


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['number_card']
    inlines = [GroupInline,]

admin.site.register(Student, StudentAdmin)
admin.site.register(Group)