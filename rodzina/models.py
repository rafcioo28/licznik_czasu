from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name='nazwa')

    class Meta:
        verbose_name = 'Nazwa'
        verbose_name_plural = 'Grupy'

    def __str__(self):
        return f'{self.name}'


class Family(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nazwisko')
    rfid = models.PositiveIntegerField(verbose_name='Kod RFID')

    class Meta:
        verbose_name = 'Rodzina'
        verbose_name_plural = 'Rodziny'

    def children_count(self):
        return self.people.filter(type_of_person='C').count()

    def get_children(self):
        return self.people.filter(type_of_person='C')

    def get_tutor(self):
        return self.people.filter(type_of_person='T')

    def __str__(self):
        return f'{self.name} [{self.rfid}]'


class Person(models.Model):
    TUTOR = 'T'
    CHILD = 'C'
    TYPE_OF_PERSON = [
        (TUTOR, 'Opiekun'),
        (CHILD, 'Dziecko')
    ]

    first_name = models.CharField(max_length=80, verbose_name='Imię')
    last_name = models.CharField(max_length=100, verbose_name='Nazwisko')
    type_of_person = models.CharField(
        max_length=1, choices=TYPE_OF_PERSON, default=CHILD,
        verbose_name="Rola w rodzinie")
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name='people',
        verbose_name='Rodzina')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='children',
        blank=True, null=True, verbose_name='Grupa')

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'

    def __str__(self):
        return f'{self.last_name} {self.first_name} - \
        {self.get_type_of_person_display()} / {self.group}'
