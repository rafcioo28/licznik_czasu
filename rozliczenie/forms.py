from django import forms


class FormRFID(forms.Form):
    rfid_number = forms.In(label='Your name', max_length=100)
