# Generated by Django 5.0.2 on 2024-02-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_alter_usuario_cedula_alter_usuario_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
