# Generated by Django 3.0.5 on 2020-08-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0014_auto_20200829_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='fav_icon',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
