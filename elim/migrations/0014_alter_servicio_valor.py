# Generated by Django 5.1.5 on 2025-02-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0013_alter_servicio_fecha_alter_servicio_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
