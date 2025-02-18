# Generated by Django 5.1.5 on 2025-02-08 17:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0006_remove_servicio_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
