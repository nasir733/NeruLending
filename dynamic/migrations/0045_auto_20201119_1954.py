# Generated by Django 3.1.1 on 2020-11-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0066_auto_20201109_1032'),
        ('dynamic', '0044_auto_20201119_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='admins',
            field=models.ManyToManyField(related_name='portals', to='user.Profile'),
        ),
    ]
