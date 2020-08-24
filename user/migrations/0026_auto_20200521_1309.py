# Generated by Django 3.0.5 on 2020-05-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20200521_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='business_city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Business City'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='business_country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Business Country'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='business_state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Business State'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='business_street_address_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Business Address Line 1'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='business_street_address_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Business Address Line 2'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='business_zip_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Business Zip Code'),
        ),
    ]
