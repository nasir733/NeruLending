# Generated by Django 3.0.5 on 2020-05-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20200501_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storecreditvendorlist',
            name='category',
        ),
        migrations.RemoveField(
            model_name='storecreditvendorlist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='storecreditvendorlist',
            name='name',
        ),
        migrations.RemoveField(
            model_name='storecreditvendorlist',
            name='report_to',
        ),
        migrations.RemoveField(
            model_name='storecreditvendorlist',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='storecreditvendorlist',
            name='url',
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='apr',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='business_revenue',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='lender_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='personal_credit_score',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='strategy',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='term_length',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='storecreditvendorlist',
            name='time_in_business',
            field=models.CharField(default='', max_length=200),
        ),
    ]