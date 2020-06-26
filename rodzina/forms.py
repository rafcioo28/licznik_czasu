from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'last_name',
            'first_name',
            'type_of_person',
            'group',
            'family',
        ]
