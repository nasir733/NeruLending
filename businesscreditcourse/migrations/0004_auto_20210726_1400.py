# Generated by Django 3.1.7 on 2021-07-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesscreditcourse', '0003_alter_businesscreditcourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscreditcourse',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
