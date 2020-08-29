from django_hosts import patterns, host
from dynamic.models import Subdomain


hosts_from_model = []
try:
    subdomains = Subdomain.objects.all()
    for i in subdomains:
        hosts_from_model.append(host(i.sub_name, 'getdinerotoday.urls', name=i.sub_name))
except Exception as e:
    pass

print(hosts_from_model)

host_patterns = patterns(
    '',
    host(r'www', 'getdinerotoday.urls', name='www'),
    *hosts_from_model,
    # host(r'businesscreditbuilders', 'getdinerotoday.urls', name='businesscreditbuilders'),
)
