from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView


from rodzina.models import Family, Person, RFID
from .forms import FormRFID


class EnterRFID(LoginRequiredMixin, FormView):
    form_class = FormRFID
    template_name = 'rozliczenie/enter_rfid.html'
    success_url = '/enter/'

    def post(self, request):
        rfid = get_object_or_404(
            RFID, rfid_number=request.POST['rfid_number'])
        family = get_object_or_404(Family, pk=rfid.family.id)
        return HttpResponseRedirect(reverse_lazy(
            'family_action', args=[family.pk]))


class FamilyAction(LoginRequiredMixin, DetailView):
    model = Family
    template_name = 'rozliczenie/children_list.html'
