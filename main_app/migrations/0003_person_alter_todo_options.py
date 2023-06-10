# Generated by Django 4.2.1 on 2023-06-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_todo_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('age', models.PositiveIntegerField()),
                ('emial', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name_plural': 'TODOes'},
        ),
    ]