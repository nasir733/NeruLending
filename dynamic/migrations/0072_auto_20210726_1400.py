# Generated by Django 3.1.7 on 2021-07-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0071_auto_20210719_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]