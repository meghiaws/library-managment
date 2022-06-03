# Generated by Django 3.2.13 on 2022-06-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_move_member_and_librarian_from_core'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='staff_code',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_code',
            field=models.CharField(max_length=8),
        ),
    ]
