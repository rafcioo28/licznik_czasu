# Generated by Django 3.0.7 on 2020-07-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rodzina', '0003_auto_20200716_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfid',
            name='rfid_number',
            field=models.PositiveIntegerField(unique=True, verbose_name='Kod RFID'),
        ),
    ]
