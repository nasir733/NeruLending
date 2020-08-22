# Generated by Django 3.0.5 on 2020-07-31 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0054_auto_20200726_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='email')),
                ('password', models.CharField(max_length=100, null=True, verbose_name='Password')),
            ],
            options={
                'verbose_name': '7. New Users',
                'verbose_name_plural': '7. New Users',
            },
        ),
    ]