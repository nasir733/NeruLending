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
from .models import Profile, UserSteps
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class GDTLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        auth_login(self.request, user)
        if user.profile.portal_goals.all().count() == 0:
            return HttpResponseRedirect("/dashboard")
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
        form = AuthenticationForm()
        return render(request, 'login.html', {"password_change_msg": "Successfully changed password", "form": form})


class MyProgressView(View):
    def get(self, request):
        request.resolver_match.app_name = 'business'
        context = {
            'source_cards': [],
            'subscriptions': []
        }
        profile = Profile.objects.get(user=request.user)
        stripe_id = profile.stripe_id
        if not stripe_id:
            stripe_user = stripe.Customer.create(
                name=f"{request.user.first_name} {request.user.last_name}",
                email=request.user.email,
            )
            profile.stripe_id = stripe_user['id']
            profile.save()
        else:
            stripe_user = stripe.Customer.retrieve(stripe_id)

        default_source = stripe_user['default_source']
        context['stripe_user'] = stripe_user
        for i in stripe_user['sources']['data']:
            if i['id'] == default_source:
                i['is_default'] = True
            context['source_cards'].append(i)

        if len(stripe_user['subscriptions']['data']) > 0:
            for i in stripe_user['subscriptions']['data']:
                names = []
                interval = ''
                total = 0

                for kk in i['items']['data']:
                    names.append(kk['price']['lookup_key'].split("_")[0])
                    interval = kk['plan']['interval']
                    total = kk['price']['unit_amount'] / 100

                sub = {
                    'name': ', '.join(names),
                    'total': total,
                    'interval': interval,
                    'subscription_id': i['id']
                }
                context['subscriptions'].append(sub)
        user_steps = UserSteps.objects.filter(user=profile)
        services = []

        for i in user_steps:

            for k in ['website', 'toll_free_number',
                      'fax_number',
                      'domain',
                      'professional_email_address']:
                if getattr(i, k) == 2:
                    serv = {
                        'name': k.replace('_', " "),
                        'status': 'In progress',
                        'product': '',
                        'dashboard': ''
                    }
                    services.append(serv)
                elif getattr(i, k) == 3:
                    dash = ''
                    if k == 'website':
                        dash = "https://www.websitebuilder.ai"
                    elif k == 'toll_free_number' or k == 'fax_number':
                        dash = "https://voip.millennialbusinessbuilders.com/login"
                    elif k == 'domain':
                        dash = getattr(i, 'domain_dashboard')
                    elif k == 'professional_email_address':
                        dash = getattr(i, 'email_provider')
                    serv = {
                        'name': k.replace('_', " "),
                        'status': 'Done',
                        'product': getattr(i, k + '_act'),
                        'dashboard': dash
                    }
                    services.append(serv)
        print(services)
        context['services'] = services
        return render(request, "my_progress.html", context=context)

    def post(self, request):
        data = request.POST
        profile = Profile.objects.get(user=request.user)
        if 'commit' in data and data['commit'] == "Save":
            user = request.user
            email_changed = data['email'] != user.email
            user.email = data['email']
            user.profile.phone_number = data['phone']
            user.save()
            user.profile.save()
            if email_changed:
                update_session_auth_hash(request, user)

        if 'delete_card' in data and data['delete_card'] == "Delete":
            if 'card' in data and data['card']:
                stripe.Customer.delete_source(
                    profile.stripe_id,
                    data['card'],
                )

        if 'create_card' in data and data['create_card'] == "Add":
            token = stripe.Token.create(
                card={
                    "number": data['cc_number'],
                    "exp_month": data['exp_month'],
                    "exp_year": data['exp_year'],
                    "cvc": data['cvc'],
                },
            )
            stripe.Customer.modify(profile.stripe_id, source=token)

        if 'cancel_subscription' in data and data['cancel_subscription'] == 'Unsubscribe':
            if 'subscription_id' in data and data['subscription_id']:
                stripe.Subscription.delete(data['subscription_id'])

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


class TermsView(View):
    def get(self, request):
        return render(request, 'terms.html')
