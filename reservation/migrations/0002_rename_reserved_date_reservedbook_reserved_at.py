# Generated by Django 3.2.13 on 2022-06-06 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservedbook',
            old_name='reserved_date',
            new_name='reserved_at',
        ),
    ]