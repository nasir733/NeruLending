# Generated by Django 3.1.1 on 2020-09-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200904_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelines',
            name='charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
            preserve_default=False,
        ),
    ]
