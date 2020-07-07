from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic.detail import SingleObjectMixin
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person, Family, Group


class ChildrenListView(LoginRequiredMixin, generic.ListView):
    model = Person
    template_name = 'rodzina/children_list.html'
    fields = [
        'first_name',
        'last_name',
        'group',
    ]

    def get_queryset(self):
        return Person.objects.filter(type_of_person='C')


class TutorListView(LoginRequiredMixin, generic.ListView):
    model = Person
    template_name = 'rodzina/tutor_list.html'
    fields = [
        'first_name',
        'last_name',
    ]

    def get_queryset(self):
        return Person.objects.filter(type_of_person='T')


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = '__all__'

    def get_success_url(self):
        if self.request.POST['type_of_person'] == 'C':
            return reverse_lazy('children')
        else:
            return reverse_lazy('tutor')


class PersonUpdate(LoginRequiredMixin, UpdateView):
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


class PersonDeleteAjax(LoginRequiredMixin, SingleObjectMixin, View):
    model = Person

    def get(self, *args, **kwargs):
        self.object = [self.get_object()]
        data = serializers.serialize("json", self.object)
        return JsonResponse(data, safe=False)

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)


class FamilyListView(generic.ListView):
    model = Family


class FamilyUpdate(UpdateView):
    model = Family
    fields = '__all__'
    success_url = reverse_lazy('family_list')


class GroupListView(generic.ListView):
    model = Group


class GrupUpdate(UpdateView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('group_list')
