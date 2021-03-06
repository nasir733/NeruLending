# Generated by Django 3.1.4 on 2021-01-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financing_portal', '0009_auto_20210121_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpurchasedmodel',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productpurchasedmodel',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productpurchasedmodel',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
