# Generated by Django 3.1.1 on 2020-12-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_tradelines_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelines',
            name='tier',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
