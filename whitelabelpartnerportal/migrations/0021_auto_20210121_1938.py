# Generated by Django 3.1.4 on 2021-01-21 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whitelabelpartnerportal', '0020_auto_20210121_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wholesale',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='wholesale',
            name='updated_at',
        ),
    ]
