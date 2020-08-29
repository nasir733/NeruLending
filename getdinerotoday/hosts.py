from django.conf import settings
from django.contrib import admin

from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'getdinerotoday.urls', name='www'),
    host(r'test', 'getdinerotoday.urls', name='test'),
    host(r'businesscreditbuilders', 'getdinerotoday.urls', name='businesscreditbuilders'),
    host(r'lawyerupmycredit', 'getdinerotoday.urls', name='lawyerupmycredit'),
    host(r'betterimagesolutions', 'getdinerotoday.urls', name='betterimagesolutions'),
)
