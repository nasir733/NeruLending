# Generated by Django 3.0.5 on 2020-05-06 15:04

import business.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200506_0825'),
        ('business', '0010_creditrepairinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCreditInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'businesscredit_information',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
    ]
