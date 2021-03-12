from django.db import migrations

from dynamic.models import Subdomain


def create_www(apps, schema_editor):
    count = Subdomain.objects.filter(sub_name='www').count()
    if count == 0:
        sub = Subdomain(
            sub_name='www'
        )
        sub.save()


class Migration(migrations.Migration):
    dependencies = [
        ('dynamic', '0054_auto_20210312_1904')
    ]

    operations = [
        migrations.RunPython(create_www),
    ]
