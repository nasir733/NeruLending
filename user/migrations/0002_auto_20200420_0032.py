# Generated by Django 3.0.3 on 2020-04-20 00:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fax_number_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='toll_free_number_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_creation_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
