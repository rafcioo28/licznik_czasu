from django.db import models
from rodzina.models import Person


class TimeCount(models.Model):
    child = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name='Dziecko')
    time_stamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Znacznik czasu')

    class Meta:
        verbose_name = 'Znacznik czasu'
        verbose_name_plural = 'Znaczniki czasu'

    def __str__(self):
        return f'{self.child.first_name} \
                {self.child.last_name} - {self.time_stamp}'
