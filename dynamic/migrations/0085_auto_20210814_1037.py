# Generated by Django 3.2.5 on 2021-08-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0084_auto_20210810_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='bcb_seo_software_bottom_heading',
            field=models.CharField(blank=True, default='Refreshing business software that your teams will love', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_seo_software_heading',
            field=models.CharField(blank=True, default='Best-in-class customer and employee engagement', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_seo_software_logo',
            field=models.CharField(blank=True, default='https://kleui.s3.amazonaws.com/documents/fe7e8fd5-3607-4e5b-b502-c5fc3819aa1e/Kleui-03-r.png', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_seo_software_logo_link',
            field=models.TextField(blank=True, default='https://bcbcrmsoftware.com/', null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_seo_software_text',
            field=models.CharField(blank=True, default='A software suite that is intuitive and easy to use so you have a happy and engaged workforce who in turn help you build and create lasting relationships with customers for life.', max_length=500, null=True),
        ),
    ]
