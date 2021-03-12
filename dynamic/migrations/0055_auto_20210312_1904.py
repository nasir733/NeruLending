from django.db import migrations

from dynamic.models import Subdomain


def create_www(apps, schema_editor):
    count = Subdomain.objects.filter(sub_name='www').count()
    if count == 0:
        sub = Subdomain(
            sub_name='www',
            logo='https://getdinerotodaybucket2.s3.amazonaws.com/documents/5291637f-891a-4e2d-a13b-c31e2f52a505/logotrans.png'
        )
        sub.save()


class Migration(migrations.Migration):
    dependencies = [
        ('dynamic', '0054_auto_20210312_1904'),
        ('user', '0073_auto_20210312_1841'),
    ]

    operations = [
        migrations.RunPython(create_www),
    ]
