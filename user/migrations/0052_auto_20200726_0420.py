# Generated by Django 3.0.5 on 2020-07-26 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0051_auto_20200721_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersteps',
            name='fax_number_amount',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Fax amount amount'),
        ),
        migrations.AddField(
            model_name='usersteps',
            name='fax_number_prefix',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Fax number prefix'),
        ),
        migrations.AddField(
            model_name='usersteps',
            name='toll_free_amount',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Toll Free amount'),
        ),
        migrations.AddField(
            model_name='usersteps',
            name='toll_free_prefix',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Toll Free prefix'),
        ),
    ]
