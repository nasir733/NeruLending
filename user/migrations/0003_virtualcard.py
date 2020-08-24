# Generated by Django 3.0.5 on 2020-05-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200420_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name="Holder's Name")),
                ('card_number', models.CharField(max_length=20, verbose_name='Card Number')),
                ('mm_yy', models.CharField(max_length=50, verbose_name='MM/YY')),
                ('cvc', models.CharField(max_length=3, verbose_name='CVC')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Zip Code')),
            ],
            options={
                'verbose_name': 'Virtual Card',
                'verbose_name_plural': 'Virtual Cards',
            },
        ),
    ]
