# Generated by Django 3.2.5 on 2021-07-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0062_auto_20210714_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='personal_credit_course_video_Heading',
            field=models.CharField(default='Personal Credit Course', help_text='add the heading for your video heading on/creditcourse/maincreditfile', max_length=200),
        ),
    ]
