from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from user.models import Portal, PortalGoal
from .models import Profile
from django.shortcuts import render
from .decorators import unauthenticated_user
from django.contrib.auth.models import User
from django.views.generic import TemplateView
import json


@method_decorator(unauthenticated_user, name='dispatch')
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'login.html', {'error': "Either username or password is incorrect"})


@method_decorator(unauthenticated_user, name='dispatch')
class SignUpView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        data = request.POST
        try:
            profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                                  data['last_name'], data['phone_number'])
            login(request, profile.user)
            return HttpResponseRedirect(reverse('homepage'))
        except Exception:
            return render(request, 'registration.html', {"error": "Registration Failed"})


class PasswordResetView(auth_views.PasswordResetView):
    @property
    def template_name(self):
        return 'forgotpassword.html'

    @property
    def success_url(self):
        return reverse('user:password_reset_done')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    @property
    def template_name(self):
        return 'resetPassword.html'

    @property
    def success_url(self):
        return reverse('user:password_change_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    @property
    def template_name(self):
        return 'password-reset-email-sent.html'


class PasswordChangeDoneView(View):
    def get(self, request):
        return render(request, 'login.html', {"password_change_msg": "Successfully changed password"})


class MyProgressView(View):
    def get(self, request):
        return render(request, "home/my_progress.html")

    def post(self, request):
        data = request.POST
        user = request.user
        email_changed = data['email'] != user.email
        user.email = data['email']
        user.profile.phone_number = data['phone']
        user.save()
        user.profile.save()
        if email_changed:
            update_session_auth_hash(request, user)
        return HttpResponseRedirect(reverse('user:myprogress'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user:login'))


class CreateSpecificPortal(TemplateView):
    template_name = "home/create_my_portal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_portals'] = Portal.objects.all()
        context['my_portals'] = PortalGoal.objects.filter(profile=self.request.user.profile)
        return context

    def post(self, request):
        data = request.POST
        name = data['name']
        portal_ids = json.loads(data['portals'])
        portal_goal = PortalGoal.objects.create(name=name, profile=request.user.profile)
        portal_goal.portals.set(portal_ids)

        return HttpResponseRedirect("/business/create-my-specific-portal/")


def delete_portal_goal(request, pk):
    try:
        obj = PortalGoal.objects.get(pk=pk)
        obj.delete()
    finally:
        return HttpResponseRedirect("/business/create-my-specific-portal/")
