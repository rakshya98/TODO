# Generated by Django 4.2.1 on 2023-06-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_emial_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
