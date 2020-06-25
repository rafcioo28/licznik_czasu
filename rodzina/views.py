from django.shortcuts import render
from django.views import generic
from .models import Person, Family, Group


class ChildrenListView(generic.ListView):
    model = Person

    def get_queryset(self):
        return Person.objects.filter(type_of_person='C')


class FamilyListView(generic.ListView):
    model = Family


class GroupListView(generic.ListView):
    model = Group
