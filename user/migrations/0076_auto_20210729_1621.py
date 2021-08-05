# Generated by Django 3.2.5 on 2021-07-29 11:21

from django.db import migrations, models
from user.models import Profile, User

# TODO  plzz move this code to the last migrations file always


def create_user(apps, schema_editor):
    user = User.objects.create_superuser(
        'adminn', email='admin@admin.com', password='123123')
    profile = Profile(user=user)
    profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0075_auto_20210726_1400'),
    ]

    operations = [

        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=models.CharField(
                blank=True, default='Signup-page', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='externalresourcecredentials',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newusercredentials',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='portalgoal',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='virtualcard',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RunPython(create_user),
    ]
