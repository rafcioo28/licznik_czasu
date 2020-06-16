from django.shortcuts import render
from django.views import generic
from .models import Person


class ChildrenListView(generic.ListView):
    model = Person

    def get_queryset(self):
        return Person.objects.filter(type_of_person='C')
