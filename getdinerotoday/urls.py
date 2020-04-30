"""getdinerotoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomePage
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.static import serve

urlpatterns = [
    path('newee_tsdsdest/', include('portals.newee_tsdsdest.urls')),
    path('newee_test/', include('portals.newee_test.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('business/', include('business.urls')),
    path('cannabis/', include('portals.cannabis.urls')),
    path('loanportal/', include('loanportal.urls')),
    path('marketingcourse/', include('marketingcourse.urls')),
    path('businesscreditcourse', include('businesscreditcourse.urls')),
    path('fitness/', include('portals.fitness.urls')),
    path('insurance_agent/', include('portals.insurance_agent.urls')),
    path('musician/', include('portals.musician.urls')),
    path('restaurant_catering/', include('portals.restaurant_catering.urls')),
    path('wedding_planner/', include('portals.wedding_planner.urls')),
    path('accountant/', include('portals.accountant.urls')),
    path('credit_repair/', include('portals.credit_repair.urls')),
    path('hair_salon/', include('portals.hair_salon.urls')),
    path('lawyer/', include('portals.lawyer.urls')),
    path('photography/', include('portals.photography.urls')),
    path('transportation/', include('portals.transportation.urls')),
    path('automotive/', include('portals.automotive.urls')),
    path('ecommerce/', include('portals.ecommerce.urls')),
    path('handy_man/', include('portals.handy_man.urls')),
    path('medical/', include('portals.medical.urls')),
    path('real_estate/', include('portals.real_estate.urls')),
    path('trucking/', include('portals.trucking.urls')),
    path('yourplan/', include('yourplan.urls')),
    path('creditcourse/', include('creditcourse.urls')),
    path('covid19/', include('covid19.urls')),
    path('affiliate/', include('affiliate.urls')),
    path('whitelabelpartnerportal/', include('whitelabelpartnerportal.urls')),
    url('^$', login_required(HomePage.as_view(), login_url='/user/login'), name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
