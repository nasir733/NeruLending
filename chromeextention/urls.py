from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ChromeExtentionIndexView
from business.urls import urlpatterns as business_urls


app_name = 'chromeextention'
urlpatterns = [

    url('^$', login_required(ChromeExtentionIndexView.as_view(), login_url='/user/login'),
        name='chromeextentionindex'),
] + business_urls[:-1]

