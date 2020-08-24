# Generated by Django 3.0.5 on 2020-04-29 12:23

import django.db.models.deletion
import yourplan.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200420_0032'),
        ('yourplan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quadpay',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='sezzle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
        migrations.CreateModel(
            name='Stripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_much_owed', models.CharField(max_length=50)),
                ('financed_so_far', models.CharField(max_length=50)),
                ('payment_left', models.CharField(max_length=50)),
                ('payment_terms', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'stripe',
            },
            bases=(yourplan.models.ModelMixin, models.Model),
        ),
    ]
