# Generated by Django 3.1.1 on 2021-02-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0050_subdomain_concierge_program_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='life_insurance_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
