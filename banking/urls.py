from django.urls import path
from . import views


urlpatterns = [
  path('',views.Index,name='banking_home'),
  path('about/',views.About,name='about'),
  path('contact/',views.Contact,name='contact'),
  path('faq/',views.Faq,name='faq'),
  path('pricing/',views.Pricing,name='pricing'),
  path('privacy-policy/',views.PrivacyPolicy,name='privacy-policy'),
  path('services/',views.Services,name='services'),
  path('terms-of-service/',views.TermsOfService,name='terms-of-service'),
]