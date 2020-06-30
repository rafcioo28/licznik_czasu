from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render, get_object_or_404, redirect, reverse
from rest_framework.response import Response
from django.views import generic
from rest_framework.views import APIView
from .forms import PersonForm, FamilyForm, GroupForm
from .models import Person, Family, Group
from .serializer import PersonSerializer


class ChildrenListView(generic.ListView):
    model = Person

    def get_queryset(self):
        return Person.objects.filter(type_of_person='C')


class FamilyListView(generic.ListView):
    model = Family


class GroupListView(generic.ListView):
    model = Group


def person_edit(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()

    return render(request, 'rodzina/person_edit.html', {'form': form})


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
