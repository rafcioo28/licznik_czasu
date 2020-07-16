# Generated by Django 3.0.7 on 2020-07-14 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rodzina', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Nazwa', 'verbose_name_plural': 'Grupy'},
        ),
        migrations.RemoveField(
            model_name='family',
            name='rfid',
        ),
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='rodzina.Group', verbose_name='Grupa'),
        ),
        migrations.CreateModel(
            name='RFID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid_number', models.PositiveIntegerField(verbose_name='Kod RFID')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family', to='rodzina.Family', verbose_name='Rodzina')),
            ],
        ),
    ]
