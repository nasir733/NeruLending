# Generated by Django 3.0.5 on 2020-05-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20200521_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='last_name',
        ),
    ]
