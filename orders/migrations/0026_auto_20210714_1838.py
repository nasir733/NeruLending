# Generated by Django 3.2.5 on 2021-07-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20210123_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelineorder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]