# Generated by Django 3.0.5 on 2020-06-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_usersteps_domain_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersteps',
            name='email_provider',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Domain name dashboard'),
        ),
    ]
