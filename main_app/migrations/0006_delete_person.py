# Generated by Django 4.2.1 on 2023-06-10 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_person_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]