# Generated by Django 3.0.5 on 2020-05-13 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whitelabelpartnerportal', '0002_becomingapartner_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whitelabelportal',
            old_name='free_portal',
            new_name='portal_link',
        ),
        migrations.RemoveField(
            model_name='whitelabelportal',
            name='paid_portal',
        ),
    ]
