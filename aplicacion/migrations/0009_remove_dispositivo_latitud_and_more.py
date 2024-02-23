# Generated by Django 5.0.2 on 2024-02-23 06:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_dispositivo_latitud_dispositivo_longitud'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivo',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='dispositivo',
            name='longitud',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='api_google_maps',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='gmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nuevo_campo',
            field=models.CharField(default='valor_predeterminado', max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
