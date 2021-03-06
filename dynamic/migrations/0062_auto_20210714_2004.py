# Generated by Django 3.2.5 on 2021-07-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0061_alter_subdomain_business_credit_course_video_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='personal_credit_course_video_Heading',
            field=models.CharField(default='Business Credit Course', help_text='add the heading for your video heading on/creditcourse/maincreditfile', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='personal_credit_course_video_link',
            field=models.CharField(blank=True, default='https://youtu.be/0JMgyfFZfiE', help_text='add the video that you want to show on the /creditcourse/maincreditfile ', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='personal_credit_course_video_link_text',
            field=models.CharField(blank=True, default='Watch The Video Above To Learn How To Use Our Credit Repair Course', help_text='add the text that you want to show on the /creditcourse/maincreditfile ', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_personal_credit_course',
            field=models.BooleanField(default=True),
        ),
    ]
