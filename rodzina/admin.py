from django.contrib import admin
from django.db import models
from .models import Family, Group, Person
from django.forms import TextInput


class FamilyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size': '30'})}
    }


admin.site.register(Person)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Group)
