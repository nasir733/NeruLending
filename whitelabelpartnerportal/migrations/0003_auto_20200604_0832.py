# Generated by Django 3.0.5 on 2020-06-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitelabelpartnerportal', '0002_auto_20200514_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whitelabelportal',
            name='portal_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
