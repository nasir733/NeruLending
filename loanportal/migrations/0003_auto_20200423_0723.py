# Generated by Django 3.0.5 on 2020-04-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanportal', '0002_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(null=True, upload_to='uploads'),
        ),
    ]
