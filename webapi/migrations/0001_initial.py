# Generated by Django 3.1.1 on 2020-09-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('number', models.IntegerField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]