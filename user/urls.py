from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import (GDTLoginView, LogoutView, MyProgressView,
                    PasswordChangeDoneView, PasswordResetConfirmView,
                    PasswordResetDoneView, PasswordResetView,
                    PortalGoalsDetailView, SignUpView, delete_portal_goal)

app_name = 'user'
urlpatterns = [
    url('login/', GDTLoginView.as_view(), name='login'),
    url('logout/', LogoutView.as_view(), name='logout'),
    url('signup/', SignUpView.as_view(), name='signup'),
    url(r'forgot-password/', PasswordResetView.as_view(email_template_name='email_templates''/reset_password_email.html'), name="password_change"),
    url(r'forgot-password-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(r'password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    url(r'forgot-passwordreset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    url('my-progress', login_required(MyProgressView.as_view(), login_url='/user/login'), name='myprogress'),
    path('delete_portal_goal/<slug:pk>/', delete_portal_goal, name='delete_portal_goal'),
    path('my-portal-goals/<slug:slug>/', PortalGoalsDetailView.as_view(), name="portal_goals"),
    url(r'my-portal-goals/[0-9A-Za-z_\-]+/', include('business.urls')),

]
