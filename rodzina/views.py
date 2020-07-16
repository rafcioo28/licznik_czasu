from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.generic.detail import SingleObjectMixin
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person, Family, Group, RFID


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


class PersonJSON(LoginRequiredMixin, SingleObjectMixin, View):
    model = Person

    def get(self, *args, **kwargs):
        self.object = [self.get_object()]
        data = serializers.serialize("json", self.object)
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        person = self.get_object()
        person.first_name = self.request.POST['first_name']
        person.last_name = self.request.POST['last_name']
        person.type_of_person = self.request.POST['type_of_person']
        person.save()
        return HttpResponse(status=204)


class PersonNewAjax(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        Person.objects.create(
            first_name=self.request.POST['first_name'],
            last_name=self.request.POST['last_name'],
            type_of_person=self.request.POST['type_of_person'],
            family=Family.objects.get(pk=self.request.POST['family'])
        )
        return HttpResponse(status=204)


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


class FamilyCreate(LoginRequiredMixin, CreateView):
    model = Family
    fields = '__all__'
    template_name = 'rodzina/family_new.html'

    def get_success_url(self):
        return reverse_lazy('family_edit', args=(self.object.id,))


class FamilyUpdate(UpdateView):
    model = Family
    fields = '__all__'
    success_url = reverse_lazy('family_list')


class RFIDNewAjax(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if not RFID.objects.filter(rfid_number=self.request.POST['rfid']):
            RFID.objects.create(
                rfid_number=self.request.POST['rfid'],
                family=Family.objects.get(pk=self.request.POST['family'])
            )
            return HttpResponse(status=204)
        message = 'Podana wartość już istnieje w bazie'
        return JsonResponse(
            status=400, data={'status': 'false', 'message': message})


class RFIDDeleteAjax(LoginRequiredMixin, SingleObjectMixin, View):
    model = RFID

    def get(self, *args, **kwargs):
        self.object = [self.get_object()]
        data = serializers.serialize("json", self.object)
        return JsonResponse(data, safe=False)

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)


class GroupListView(generic.ListView):
    model = Group


class GrupUpdate(UpdateView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('group_list')
