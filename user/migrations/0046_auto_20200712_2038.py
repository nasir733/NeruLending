# Generated by Django 3.0.5 on 2020-07-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0045_usersteps_business_builder_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersteps',
            name='business_builder_program',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1, null=True, verbose_name='Business Builder Program'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='professional_email_address_act',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Actual professional email address'),
        ),
    ]