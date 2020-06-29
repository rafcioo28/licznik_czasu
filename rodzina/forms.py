from django.forms import ModelForm
from .models import Person, Family, Group


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


class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = [
            'name',
            'rfid',
        ]


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
        ]
