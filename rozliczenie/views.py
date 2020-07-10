from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class EnterRFID(LoginRequiredMixin, View):
    form_rfid = FormRFID
    template_name = 'rozenter_rfid.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
