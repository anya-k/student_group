from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from groups.models import Group


class GroupListView(ListView):
    model = Group


class GroupDetailView(DetailView):
    model = Group


class GroupCreateView(CreateView):
    model = Group


class GroupUpdateView(UpdateView):
    model = Group


class GroupDeleteView(DeleteView):
    model = Group