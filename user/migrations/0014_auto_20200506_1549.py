# Generated by Django 3.0.5 on 2020-05-06 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_portalgoal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portalgoal',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portal_goals', to='user.Profile'),
        ),
    ]
