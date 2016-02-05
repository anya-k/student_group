# -*- coding: utf-8 -*-
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from students.models import Student
from students.forms import StudentForm
from groups.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StudentListView(generic.ListView):
    model = Student

    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset()
        group_id = self.request.GET.get('group_id')
        if group_id:
            queryset = queryset.filter(group=int(group_id))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super(StudentListView, self).get_context_data(**kwargs)
        group_id = self.request.GET.get('group_id')
        groups_with_headman = Group.objects.exclude(headman__isnull=True)
        headmans = []
        h2_text = "Список всех студентов"
        for group in groups_with_headman:
            headmans.append(group.headman)
        if group_id:
            selected_group = Group.objects.filter(id=group_id)
            headmans = []
            for group in selected_group:
                headmans.append(group.headman)
                h2_text = u"Список студентов группы {0}".format(group.name)
        context_data['headmans'] = headmans
        context_data['h2_text'] = h2_text
        return context_data


class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context_data = super(StudentDetailView, self).get_context_data(**kwargs)
        is_headman = Group.objects.filter(headman=self.object.id)
        context_data['is_headman'] = is_headman.count()
        return context_data


@method_decorator(login_required, name='dispatch')
class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def get_context_data(self, **kwargs):
        context_data = super(StudentCreateView, self).get_context_data(**kwargs)
        context_data['page_title'] = "Создание студента"
        context_data['h3_title'] = "Создание"
        context_data['cancel_url'] = reverse_lazy('students:index')
        return context_data

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, u'Студент {0} успешно добавлен'.format(self.object.full_name()))
        return response


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def get_context_data(self, **kwargs):
        context_data = super(StudentUpdateView, self).get_context_data(**kwargs)
        context_data['page_title'] = "Изменение студента"
        context_data['h3_title'] = "Редактирование"
        context_data['cancel_url'] = reverse_lazy('students:index')
        return context_data

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u'Студент {0} успешно изменен'.format(self.object.full_name()))
        return response


class StudentDeleteView(generic.DeleteView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, u'Студент {0} успешно удален'.format(self.object.full_name()))
        return response
