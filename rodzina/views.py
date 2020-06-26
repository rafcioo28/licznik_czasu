from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import PersonForm
from .models import Person, Family, Group


class ChildrenListView(generic.ListView):
    model = Person

    def get_queryset(self):
        return Person.objects.filter(type_of_person='C')


def person_edit(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)

    return render(request, 'rodzina/person_edit.html', {'form': form})


class FamilyListView(generic.ListView):
    model = Family


class GroupListView(generic.ListView):
    model = Group
