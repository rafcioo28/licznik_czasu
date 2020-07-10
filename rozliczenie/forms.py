from django import forms


class FormRFID(forms.Form):
    rfid_number = forms.IntegerField(label='RFID')
