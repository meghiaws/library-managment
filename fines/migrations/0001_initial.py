# Generated by Django 3.2.13 on 2022-06-07 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrowing', '0002_alter_borrowedbook_borrower'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('borrowed_book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='borrowing.borrowedbook')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
    ]
