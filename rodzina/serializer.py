from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'type_of_person',
            'family',
        ]
