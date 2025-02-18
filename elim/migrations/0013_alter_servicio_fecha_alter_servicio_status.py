# Generated by Django 5.1.5 on 2025-02-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0012_servicio_numero_registo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='status',
            field=models.CharField(choices=[('creado', 'Creado'), ('ejecutado', 'Ejecutado'), ('cotizado', 'Cotizado'), ('facturado', 'Facturado'), ('no_show', 'NO SHOW')], default='creado', help_text='Status', max_length=15),
        ),
    ]
