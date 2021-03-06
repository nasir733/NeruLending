# Generated by Django 3.0.5 on 2020-05-13 16:02

from django.db import migrations, models
import marketingcourse.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('report_to', models.CharField(max_length=50, null=True)),
                ('monthly_payment', models.CharField(max_length=15, null=True)),
                ('estimated_term', models.CharField(max_length=50, null=True)),
                ('estimated_amount', models.CharField(max_length=5, null=True)),
                ('payment_terms', models.CharField(max_length=50, null=True)),
                ('terms', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'marketingcourse',
            },
            bases=(marketingcourse.models.ModelMixin, models.Model),
        ),
    ]
