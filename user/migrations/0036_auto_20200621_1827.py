# Generated by Django 3.0.5 on 2020-06-21 18:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0035_auto_20200621_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersteps',
            old_name='professional_email',
            new_name='professional_email_address',
        ),
    ]
