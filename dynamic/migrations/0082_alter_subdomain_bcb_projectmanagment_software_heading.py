# Generated by Django 3.2.5 on 2021-08-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0081_subdomain_bcb_projectmanagment_software_logo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='bcb_projectmanagment_software_heading',
            field=models.CharField(blank=True, default='bcbprojectmanagment helps teams move work forward.', max_length=500, null=True),
        ),
    ]
