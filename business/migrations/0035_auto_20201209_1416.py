# Generated by Django 3.1.1 on 2020-12-09 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0034_auto_20201209_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tier1',
            old_name='amount',
            new_name='tradeline_amount',
        ),
        migrations.RenameField(
            model_name='tier2',
            old_name='amount',
            new_name='tradeline_amount',
        ),
        migrations.RenameField(
            model_name='tier3',
            old_name='amount',
            new_name='tradeline_amount',
        ),
        migrations.RenameField(
            model_name='tier4',
            old_name='amount',
            new_name='tradeline_amount',
        ),
    ]
