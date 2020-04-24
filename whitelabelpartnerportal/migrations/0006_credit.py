# Generated by Django 3.0.5 on 2020-04-22 20:33

from django.db import migrations, models
import django.db.models.deletion
import whitelabelpartnerportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200420_0032'),
        ('whitelabelpartnerportal', '0005_affiliateresidual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=50, null=True)),
                ('created', models.CharField(max_length=50)),
                ('applied', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whitelabelpartnerportalcredit_profile', to='user.Profile')),
            ],
            options={
                'db_table': 'whitelabelpartnerportal_credit',
            },
            bases=(whitelabelpartnerportal.models.ModelMixin, models.Model),
        ),
    ]
