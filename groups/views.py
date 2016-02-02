# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from groups.models import Group
from groups.forms import GroupForm, GroupUpdateForm
from students.models import Student


class GroupListView(ListView):
    model = Group


class GroupDetailView(DetailView):
    model = Group


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy('groups:index')

    def get_context_data(self, **kwargs):
        context_data = super(GroupCreateView, self).get_context_data(**kwargs)
        context_data['page_title'] = "Создание группы"
        context_data['h3_title'] = "Создание"
        context_data['cancel_url'] = reverse_lazy('groups:index')
        return context_data

    def form_valid(self, form):
        response = super(GroupCreateView, self).form_valid(form)
        messages.success(self.request, u'Группа {0} успешно добавлена'.format(self.object.name))
        return response


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy('groups:index')

    def get_object(self, queryset=None):
        object = super(GroupUpdateView, self).get_object(queryset)
        self.request.cur_object = object
        return object

    def get_form(self, form_class=None):
        form = super(GroupUpdateView, self).get_form(form_class)
        if self.request.cur_object:
            form.fields["headman"].queryset = Student.objects.filter(group=self.request.cur_object.id)
        else:
            form.fields["headman"].queryset = Student.objects.filter(group=None)
        return form

    def get_context_data(self, **kwargs):
        context_data = super(GroupUpdateView, self).get_context_data(**kwargs)
        context_data['page_title'] = "Изменение группы"
        context_data['h3_title'] = "Редактирование"
        context_data['cancel_url'] = reverse_lazy('groups:index')
        return context_data

    def form_valid(self, form):
        response = super(GroupUpdateView, self).form_valid(form)
        messages.success(self.request, u'Группа {0} успешно изменена'.format(self.object.name))
        return response


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:index')

    def delete(self, request, *args, **kwargs):
        response = super(GroupDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, u'Группа {0} успешно удалена'.format(self.object.name))
        return response