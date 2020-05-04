# Generated by Django 3.0.3 on 2020-04-26 20:54

from django.db import migrations, models
import django.db.models.deletion
import loanportal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200420_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('interest_rate', models.CharField(max_length=500, null=True)),
                ('term_length', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loansportalloan_profile', to='user.Profile')),
            ],
            options={
                'db_table': 'Loan',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
                ('document', models.FileField(null=True, upload_to=loanportal.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loansportaldocument_profile', to='user.Profile')),
            ],
            options={
                'db_table': 'Document',
            },
        ),
    ]
