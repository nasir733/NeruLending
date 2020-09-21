from django.urls.resolvers import get_resolver
from django_hosts import patterns, host


class HostsService:

    @classmethod
    def update_hosts_conf(cls):
        from getdinerotoday.middleware.hosts import HostsBaseMiddleware
        if hasattr(get_resolver(None), 'urlconf_module'):
            delattr(get_resolver(None), 'urlconf_module')
        HostsBaseMiddleware.update_host_patters()

    @classmethod
    def get_host_patterns(cls):
        from dynamic.models import Subdomain
        hosts_from_model = []
        try:
            subdomains = Subdomain.objects.all()
            for i in subdomains:
                hosts_from_model.append(host(i.sub_name, 'getdinerotoday.urls', name=i.sub_name))
        except Exception as e:
            pass
        new_host_patterns = patterns(
            '',
            host(r'www', 'getdinerotoday.urls', name='www'),
            *hosts_from_model,
            # host(r'businesscreditbuilders', 'getdinerotoday.urls', name='businesscreditbuilders'),
        )
        return new_host_patterns
