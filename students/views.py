from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from students.forms import StudentForm
from groups.models import Group

class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context_data = super(StudentDetailView, self).get_context_data(**kwargs)
        is_headman = Group.objects.filter(headman=self.object.id)
        context_data['is_headman'] = is_headman.count()
        return context_data


class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')


class StudentDeleteView(generic.DeleteView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')
