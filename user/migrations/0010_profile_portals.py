# Generated by Django 3.0.5 on 2020-05-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0009_auto_20200506_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='portals',
            field=models.ManyToManyField(related_name='portals_subscribed', to='user.Portal'),
        ),
    ]
