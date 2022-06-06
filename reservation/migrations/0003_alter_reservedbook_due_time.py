# Generated by Django 3.2.13 on 2022-06-06 16:00

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_rename_reserved_date_reservedbook_reserved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedbook',
            name='due_time',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(django.utils.timezone.now)]),
        ),
    ]
