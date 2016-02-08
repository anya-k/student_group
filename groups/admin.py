from django.contrib import admin

from .models import Group
from students.models import Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_person')
    inlines = [StudentInline,]

    def get_form(self, request, obj=None, **kwargs):
        request.current_object = obj
        return super(GroupAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        instance = request.current_object
        if db_field.name == "headman":
            if instance:
                kwargs["queryset"] = Student.objects.filter(group=instance.id)
            else:
                kwargs["queryset"] = Student.objects.filter(group=None)
        return super(GroupAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Group, GroupAdmin)