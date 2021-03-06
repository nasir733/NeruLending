# Generated by Django 3.0.5 on 2020-10-11 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0024_auto_20200929_1618'),
        ('products', '0020_auto_20200920_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelines',
            name='whitelabel_portal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic.Subdomain'),
        ),
        migrations.AlterField(
            model_name='userstepsproduct',
            name='whitelabel_portal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic.Subdomain'),
        ),
    ]
