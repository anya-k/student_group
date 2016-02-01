from django.contrib import admin

from .models import Student, Group


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['group']
    search_fields = ['number_card']
    inlines = [GroupInline,]


class GroupAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        request.current_object = obj
        return super(GroupAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        instance = request.current_object
        if db_field.name == "headman":
            kwargs["queryset"] = Student.objects.filter(group=instance.id)
        return super(GroupAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)