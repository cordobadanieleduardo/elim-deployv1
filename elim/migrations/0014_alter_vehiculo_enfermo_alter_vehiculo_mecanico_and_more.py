# Generated by Django 5.1.6 on 2025-03-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0013_alter_gastoconductor_estado_aceptacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='enfermo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='mecanico',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='restaurante',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
