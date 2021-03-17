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
        has_www = False
        try:
            subdomains = Subdomain.objects.all()
            for i in subdomains:
                if i.sub_name == 'www':
                    has_www = True
                else:
                    hosts_from_model.append(host(i.sub_name, 'getdinerotoday.urls', name=i.sub_name))
        except Exception as e:
            pass

        # print(hosts_from_model)
        if not has_www:
            new_host_patterns = patterns(
                '',
                *hosts_from_model,
                host(r'www', 'getdinerotoday.urls', name='www'),
            )
        else:
            new_host_patterns = patterns(
                '',
                *hosts_from_model,
            )

        return new_host_patterns
