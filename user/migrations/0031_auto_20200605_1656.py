# Generated by Django 3.0.5 on 2020-06-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0030_auto_20200605_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersteps',
            name='domain',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1,
                                      null=True, verbose_name='Domain'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='fax_number',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1,
                                      null=True, verbose_name='Fax numberx'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='professional_email',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1,
                                      null=True, verbose_name='Professional email'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='toll_free',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1,
                                      null=True, verbose_name='Toll free number'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='website',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1,
                                      null=True, verbose_name='Website'),
        ),
    ]
