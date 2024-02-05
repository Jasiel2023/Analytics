# Generated by Django 4.2.8 on 2024-01-28 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DISPOSITIVOS',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='infoUsuario',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='resultadosAlmacenados',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='usuario',
        ),
        migrations.AddField(
            model_name='informe',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medidordeconsumo',
            name='registro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='medidorDeConsumo', to='aplicacion.registro'),
            preserve_default=False,
        ),
    ]