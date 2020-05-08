import json

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
# from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView
from user.models import Portal, PortalGoal

from .decorators import unauthenticated_user
from .models import Profile


class GDTLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        auth_login(self.request, user)
        if user.profile.portal_goals.all().count() == 0:
            return HttpResponseRedirect("/business/create-my-specific-portal/")
        else:
            return HttpResponseRedirect(user.profile.portal_goals.first().get_absolute_url())


@method_decorator(unauthenticated_user, name='dispatch')
class SignUpView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        data = request.POST
        try:
            profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                                  data['last_name'], data['phone_number'])
            auth_login(request, profile.user)
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
        return render(request, "my_progress.html")

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
    template_name = "goals/create_my_portal.html"

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


class PortalGoalsDetailView(LoginRequiredMixin, DetailView):
    model = PortalGoal
    template_name = "goals/portal_goals.html"
    context_object_name = 'portal_goal'

    def get_object(self):
        try:
            obj = PortalGoal.objects.get(slug=self.kwargs['slug'])
            return obj
        except PortalGoal.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(PortalGoalsDetailView, self).get_context_data(**kwargs)
        if 'slug' in self.kwargs:
            context['portal_number'] = self.kwargs['slug']
        return context