from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PersonSerializer

from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import PersonForm, FamilyForm, GroupForm
from .models import Person, Family, Group


class ChildrenListView(generic.ListView):
    model = Person
    template_name = 'rodzina/children_list.html'
    fields = [
        'first_name',
        'last_name',
        'group',
    ]

    def get_queryset(self):
        return Person.objects.filter(type_of_person='C')


class TutorListView(generic.ListView):
    model = Person
    template_name = 'rodzina/tutor_list.html'
    fields = [
        'first_name',
        'last_name',
    ]

    def get_queryset(self):
        return Person.objects.filter(type_of_person='T')


class FamilyListView(generic.ListView):
    model = Family


class GroupListView(generic.ListView):
    model = Group


class PersonUpdate(UpdateView):
    model = Person
    fields = [
        'first_name',
        'last_name',
        'type_of_person',
        'family',
        'group',
    ]

    def get_success_url(self):
        if self.request.POST['type_of_person'] == 'C':
            return reverse_lazy('children')
        else:
            return reverse_lazy('tutor')


class PersonViewAPI(APIView):

    def get(self, request, person_id):
        person = Person.objects.filter(id=person_id).first()
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    def post(self, request, person_id):
        person = Person.objects.filter(id=person_id).first()
        serializer = PersonSerializer(person, data=request.data)
        # person.last_name = request.PUT['last_name']
        # person.first_name = request.PUT['first_name']
        # person.type_of_person = request.PUT['type_of_person']
        if serializer.is_valid():
            print('serializer is valid')

        # person.save()
        return redirect(reverse('family_edit', args=[person.family.id]))


def family_edit(request, id):
    family = get_object_or_404(Family, pk=id)
    form = FamilyForm(request.POST or None, instance=family)

    if form.is_valid():
        form.save()

    return render(
        request,
        'rodzina/family_edit.html',
        {'form': form, 'family': family})


def group_edit(request, id):
    group = get_object_or_404(Group, pk=id)
    form = GroupForm(request.POST or None, instance=group)

    if form.is_valid():
        form.save()

    return render(request, 'rodzina/group_edit.html', {'form': form})
