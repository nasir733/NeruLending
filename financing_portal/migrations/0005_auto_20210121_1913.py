# Generated by Django 3.1.4 on 2021-01-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financing_portal', '0004_merge_20210121_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='recurring',
            field=models.CharField(choices=[('month', 'month'), ('year', 'year'), ('one_time', 'one_time')], default=('month', 'month'), max_length=10),
        ),
    ]
