# Generated by Django 3.2.5 on 2021-08-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0073_alter_subdomain_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='bcb_video_software_heading',
            field=models.CharField(blank=True, default='Simple tools for any professional, team, and organization to\ncreate, manage, and share high-quality videos.', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_video_software_logo',
            field=models.CharField(blank=True, default='https://kleui.s3.amazonaws.com/documents/fe7e8fd5-3607-4e5b-b502-c5fc3819aa1e/Kleui-03-r.png', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_video_software_logo_link',
            field=models.TextField(blank=True, default='https://bcbvideosoftware.com/', null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='bcb_video_software_text',
            field=models.CharField(blank=True, default='Unlock the\n                                               power of video', max_length=500, null=True),
        ),
    ]
