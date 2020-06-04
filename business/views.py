from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from user.forms import UserDataForm
from user.models import PortalGoal, UserData
from .forms import BusinessCreditStepsForm
from .models import *

portal_list = {
    "business": "",
    "fitness": "Fitness",
    "accountant": "Accountant",
    "automotive": "Automotive",
    "cannabis": "cannabis",
    "credit_repair": "credit repair",
    "ecommerce": "ecommerce",
    "hair_salon": "hair salon",
    "handy_man": "handy man",
    "insurance_agent": "insurance agent",
    "lawyer": "lawyer",
    "medical": "medical",
    "musician": "musician",
    "photography": "photography",
    "real_estate": "real estate",
    "restaurant_catering": "restaurant and catering",
    "transportation": "transportation",
    "trucking": "trucking",
    "wedding_planner": "wedding planner",
    "goals": "Goals",
    "chromeextension": "chromeextension",
    "user": "User",
    "user:business": "User"
}


def get_business_plan_context():
    lenders = Lender.objects.all()
    store_credits = StoreCreditVendorList.objects.all()
    revolvings = RevolvingCredit.objects.all()
    nopgs = Nopg.objects.all()
    context = {
        "lenders": lenders,
        "store_credits": store_credits,
        "revolvings": revolvings,
        "nopgs": nopgs,
    }

    return context


def get_context_for_all(request, context=None):
    app_name = request.resolver_match.app_name
    if not context:
        context = {}
    context["verbose_portal_name"] = portal_list[app_name]
    if not hasattr(request.resolver_match, 'page_template'):
        request.resolver_match.page_template = 'pages/base-business.html'

    if request.resolver_match.app_name == 'user:business':
        request.resolver_match.page_template = 'goals/goals_base.html'
        slug = request.path.split('/my-portal-goals/')[1].split("/")[0]
        obj = PortalGoal.objects.get(slug=slug)
        context['portal_goal'] = obj
        print()
        context['portal_number'] = slug

    if request.resolver_match.app_name == 'chromeextension':
        request.resolver_match.page_template = 'base-chromeextension.html'

    return context


class BusinessHomePage(View):
    def get(self, request):
        return render(request, f"index-{request.resolver_match.app_name}.html",
                      context=get_context_for_all(request, get_business_plan_context()))


class BusinessCreditStepsView(View):
    def get(self, request):
        template = "userData/BusinessCreditSteps.html"
        if "standalone" in request.path:
            template = "userData/BusinessCreditStepsStandalone.html"

        form = BusinessCreditStepsForm()
        return render(request, template, context=get_context_for_all(request, {"form": form}))

    def post(self, request):
        template = "userData/BusinessCreditSteps.html"
        if "standalone" in request.path:
            template = "userData/BusinessCreditStepsStandalone.html"
        form = BusinessCreditStepsForm(request.POST)
        new_data = form.save(commit=False)
        new_data.user = Profile.objects.get(user=request.user)
        new_data.save()
        form = BusinessCreditStepsForm()
        return render(request, template, context=get_context_for_all(request, {"form": form}))


class UserDataView(View):
    def get(self, request):

        data = UserData.objects.filter(user=Profile.objects.get(user=request.user))
        if len(data) > 0:
            data = data[0]
            form = UserDataForm(None, instance=data)
        else:
            form = UserDataForm()
        return render(request, "userData/userData.html", context=get_context_for_all(request, {"form": form}))

    def post(self, request):
        data = UserData.objects.filter(user=Profile.objects.get(user=request.user))
        if len(data) > 0:
            data = data[0]
            form = UserDataForm(request.POST, instance=data)
            new_data = form.save(commit=False)
            new_data.user = Profile.objects.get(user=request.user)
            new_data.save()
        else:
            form = UserDataForm(request.POST)
            new_data = form.save(commit=False)
            new_data.user = Profile.objects.get(user=request.user)
            new_data.save()

        data = UserData.objects.filter(user=Profile.objects.get(user=request.user))
        form = UserDataForm(None, instance=data[0])
        return render(request, "userData/userData.html", context=get_context_for_all(request, {"form": form}))


class BusinessPlan1View(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "home/businessplan1.html",
                      context=get_context_for_all(request, get_business_plan_context()))


class BusinessPlan2View(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "home/businessplan2.html",
                      context=get_context_for_all(request, get_business_plan_context()))


class BusinessPlan3View(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "home/businessplan3.html",
                      context=get_context_for_all(request, get_business_plan_context()))


class BusinessCreditBuildingPlanView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        return render(request, "home/business.html", context=get_context_for_all(request))

    def post(self, request):
        data = request.POST
        business_time = int(data['business_time'])
        trade_lines = int(data['trade_lines'])

        dic1 = {
            1: "Less Than 1 year",
            2: "1 Year - 2 Years",
            3: "3 years Or More",
        }

        dic2 = {
            1: "4 Or Less Tradelines Reporting",
            2: "5-9 Tradelines Reporting",
            3: "10 or More Tradelines Reporting",
        }

        dic = {
            'business_time': dic1[business_time],
            'trade_lines': dic2[trade_lines]
        }

        information = BusinessCreditInformation(user=Profile.objects.get(user=request.user), **dic)
        information.save()
        path = '/'.join(request.path.split("/")[:-3]) + "/"

        if business_time == 1:
            if trade_lines == 1:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_1"))
                return HttpResponseRedirect(path + 'business-plan-1')
            elif trade_lines == 2:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_2"))
                return HttpResponseRedirect(path + 'business-plan-2')

            elif trade_lines == 3:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_3"))
                return HttpResponseRedirect(path + 'business-plan-3')

        elif business_time == 2:
            if trade_lines == 1:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_1"))
                return HttpResponseRedirect(path + 'business-plan-1')
            elif trade_lines == 2:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_2"))
                return HttpResponseRedirect(path + 'business-plan-2')
            elif trade_lines == 3:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_3"))
                return HttpResponseRedirect(path + 'business-plan-3')
        elif business_time == 3:
            if trade_lines == 1:
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_1"))
                return HttpResponseRedirect(path + 'business-plan-1')
            elif trade_lines == 2:
                return HttpResponseRedirect(path + 'business-plan-1')
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(path + 'business-plan-1')
                # return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:business_plan_3"))


class UpgradeView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "home/upgrade.html", context=get_context_for_all(request))


class RestrictedView(View):
    def get(self, request):
        return render(request, "home/restricted.html", context=get_context_for_all(request))


class GoalView(View):
    def get(self, request):
        request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "businessCreditBuilding/goals.html", context=get_context_for_all(request))


class FinancingView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'financing.html', context=get_context_for_all(request))

    def post(self, request):
        data = request.POST
        experian = int(data['experian'])
        equifax = int(data['equifax'])
        transunion = int(data['transunion'])
        monthly_revenue_3 = int(data['monthly_revenue_3'])
        daily_balance_3 = int(data['daily_balance_3'])
        monthlty_ending_balance_3 = int(data['monthlty_ending_balance_3'])
        monthly_revenue_6 = int(data['monthly_revenue_6'])
        daily_balance_6 = int(data['daily_balance_6'])
        monthlty_ending_balance_6 = int(data['monthlty_ending_balance_6'])
        business_revenue = int(data['business_revenue'])
        nonsufficient_6 = int(data['nonsufficient_6'])
        nonsufficient_12 = int(data['nonsufficient_12'])
        current_liens = int(data['current_liens'])
        business_account = int(data['business_account'])
        business_loan = int(data['business_loan'])
        business_age = int(data['business_age'])

        dic1 = {
            1: "599 or below",
            2: "600-679",
            3: "680+ Credit Score or Higher"
        }

        dic2 = {
            1: "$3499 or below",
            2: "$3500 or above"
        }

        dic3 = {
            1: "$499 or below",
            2: "$500 or above"
        }

        dic4 = {
            1: "$41,999 or below",
            2: "$42,000 - $99,000",
            3: "$100,000 or above"
        }

        dic5 = {
            1: "Yes",
            2: "No"
        }

        dic6 = {
            1: "Less Than 3 Months Ago",
            2: "3 Months - 8 Months",
            3: "9 Months - 11 Months",
            4: "1 Year - 2 Years",
            5: "3 years Or More",
        }

        dic = {'experian': dic1[experian],
               'equifax': dic1[equifax],
               'transunion': dic1[transunion],
               'monthly_revenue_3': dic2[monthly_revenue_3],
               'daily_balance_3': dic3[daily_balance_3],
               'monthlty_ending_balance_3': dic3[monthlty_ending_balance_3],
               'monthly_revenue_6': dic2[monthly_revenue_6],
               'daily_balance_6': dic3[daily_balance_6],
               'monthlty_ending_balance_6': dic3[monthlty_ending_balance_6],
               'business_revenue': dic4[business_revenue],
               'nonsufficient_6': dic5[nonsufficient_6],
               'nonsufficient_12': dic5[nonsufficient_12],
               'current_liens': dic5[current_liens],
               'business_account': dic5[business_account],
               'business_loan': dic5[business_loan],
               'business_age': dic6[business_age]}

        information = FinancingInformation(user=Profile.objects.get(user=request.user), **dic)
        information.save()
        path = '/'.join(request.path.split("/")[:-2]) + "/"

        # if experian == 1:
        #     if monthly_revenue_3 == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_8"))
        #     else:
        #         if business_age == 5:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_12"))
        #         else:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_1"))
        # if experian == 2:
        #     if monthly_revenue_3 == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_7"))
        #     elif monthly_revenue_3 == 2:
        #         if business_age == 5:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_15"))
        #     else:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_2"))
        #
        # if experian == 3:
        #     if monthly_revenue_3 == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_6"))
        #     else:
        #         if business_age <= 4:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_3"))
        #         else:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:financing_plan_10"))

        if experian == 1:
            if monthly_revenue_3 == 1:
                return HttpResponseRedirect(path + "financing-plan-8")
            else:
                if business_age == 5:
                    return HttpResponseRedirect(path + "financing-plan-12")
                else:
                    return HttpResponseRedirect(path + "financing-plan-1")
        if experian == 2:
            if monthly_revenue_3 == 1:
                return HttpResponseRedirect(path + "financing-plan-7")
            elif monthly_revenue_3 == 2:
                if business_age == 5:
                    return HttpResponseRedirect(path + "financing-plan-15")
            else:
                return HttpResponseRedirect(path + "financing-plan-2")

        if experian == 3:
            if monthly_revenue_3 == 1:
                return HttpResponseRedirect(path + "financing-plan-6")
            else:
                if business_age <= 4:
                    return HttpResponseRedirect(path + "financing-plan-3")
                else:
                    return HttpResponseRedirect(path + "financing-plan-10")


class FinancingPlan1View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan1.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trls'] = []
        context['locs'] = []
        context['lenders'] = Lender.objects.all()
        context['invoices'] = []
        context['finance_invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan2View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan2.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        context['trls'] = []
        context['locs'] = []
        context['lenders'] = []
        context['invoices'] = []
        context['finance_invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan3View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan3.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        context['locs'] = []
        context['sba_loans'] = []
        context['invoices'] = []
        context['finance_invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan6View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan6.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenders'] = []
        context['equipments'] = []
        return context


class FinancingPlan7View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan7.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenders'] = []
        context['invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan8View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan8.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenders'] = []
        context['equipments'] = []
        return context


class FinancingPlan10View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan10.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        context['trls'] = []
        context['locs'] = []
        context['lenders'] = []
        context['sba_loans'] = []
        context['invoices'] = []
        context['finance_invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan12View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan12.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        context['trls'] = []
        context['locs'] = []
        context['lenders'] = []
        context['invoices'] = []
        context['finance_invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan15View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "financingplans/financingplan15.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        context['trls'] = []
        context['locs'] = []
        context['lenders'] = []
        context['sba_loans'] = []
        context['invoices'] = []
        context['finance_invoices'] = []
        context['equipments'] = []
        return context


class CreditSituationView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "home/creditsituation.html", context=get_context_for_all(request))

    def post(self, request):
        data = request.POST
        experian_score = int(data['experian_score'])
        equifax_score = int(data['equifax_score'])
        transunion_score = int(data['transunion_score'])
        experian_utilization = int(data['experian_utilization'])
        equifax_utilization = int(data['equifax_utilization'])
        transunion_utilization = int(data['transunion_utilization'])
        current_collections = int(data['current_collections'])
        bankruptcies = int(data['bankruptcies'])
        bankruptcies_10 = int(data['bankruptcies_10'])
        inquiries = int(data['inquiries'])
        missed_payments = int(data['missed_payments'])
        current_acc_experian = int(data['current_acc_experian'])
        current_acc_equifax = int(data['current_acc_equifax'])
        current_acc_transunion = int(data['current_acc_transunion'])
        credit_history_experian = int(data['credit_history_experian'])
        credit_history_equifax = int(data['credit_history_equifax'])
        credit_history_transunion = int(data['credit_history_transunion'])

        dic1 = {
            1: "599 or below",
            2: "600-679",
            3: "680+ Credit Score or Higher"
        }

        dic5 = {
            1: "Yes",
            2: "No"
        }

        dic7 = {
            1: '30% Or Lower',
            2: '31% Or More'
        }

        dic8 = {
            1: '3 Or Less',
            2: '4 Or More'
        }
        dic9 = {
            1: '2 years Or Less',
            2: '3 years Or More'
        }

        data_dict = {
            'experian_score': dic1[experian_score],
            'equifax_score': dic1[equifax_score],
            'transunion_score': dic1[transunion_score],
            'experian_utilization': dic7[experian_utilization],
            'equifax_utilization': dic7[equifax_utilization],
            'transunion_utilization': dic7[transunion_utilization],
            'current_collections': dic5[current_collections],
            'bankruptcies': dic5[bankruptcies],
            'bankruptcies_10': dic5[bankruptcies_10],
            'inquiries': dic5[inquiries],
            'missed_payments': dic5[missed_payments],
            'current_acc_experian': dic8[current_acc_experian],
            'current_acc_equifax': dic8[current_acc_equifax],
            'current_acc_transunion': dic8[current_acc_transunion],
            'credit_history_experian': dic9[credit_history_experian],
            'credit_history_equifax': dic9[credit_history_equifax],
            'credit_history_transunion': dic9[credit_history_transunion],
        }

        new_info = CreditRepairInformation(user=Profile.objects.get(user=request.user), **data_dict)
        new_info.save()
        path = '/'.join(request.path.split("/")[:-2]) + "/"

        # if experian_score == 1:
        #     if bankruptcies_10 == 1:
        #         if credit_history_experian == 1:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_1"))
        #         else:
        #             # a tie btn 4 and 7
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_7"))
        #     if inquiries == 2:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_14"))
        #     else:
        #         if missed_payments == 1:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_8"))
        #         else:
        #             return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_11"))
        # elif experian_score == 2:
        #     if bankruptcies_10 == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_5"))
        #     if inquiries == 2:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_15"))
        #     if missed_payments == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_9"))
        #     if missed_payments == 2:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_12"))
        #     else:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_17"))
        #
        # else:
        #     if bankruptcies_10 == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_6"))
        #     if inquiries == 2:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_16"))
        #     if missed_payments == 1:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_10"))
        #     if missed_payments == 2:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_13"))
        #     else:
        #         return HttpResponseRedirect(reverse(f"{request.resolver_match.app_name}:credit_repair_17"))

        if experian_score == 1:
            if bankruptcies_10 == 1:
                if credit_history_experian == 1:
                    return HttpResponseRedirect(path + "credit-repair-1")
                else:
                    # a tie btn 4 and 7
                    return HttpResponseRedirect(path + "credit-repair-7")
            if inquiries == 2:
                return HttpResponseRedirect(path + "credit-repair-14")
            else:
                if missed_payments == 1:
                    return HttpResponseRedirect(path + "credit-repair-8")
                else:
                    return HttpResponseRedirect(path + "credit-repair-11")
        elif experian_score == 2:
            if bankruptcies_10 == 1:
                return HttpResponseRedirect(path + "credit-repair-5")
            if inquiries == 2:
                return HttpResponseRedirect(path + "credit-repair-15")
            if missed_payments == 1:
                return HttpResponseRedirect(path + "credit-repair-9")
            if missed_payments == 2:
                return HttpResponseRedirect(path + "credit-repair-12")
            else:
                return HttpResponseRedirect(path + "credit-repair-17")

        else:
            if bankruptcies_10 == 1:
                return HttpResponseRedirect(path + "credit-repair-6")
            if inquiries == 2:
                return HttpResponseRedirect(path + "credit-repair-16")
            if missed_payments == 1:
                return HttpResponseRedirect(path + "credit-repair-10")
            if missed_payments == 2:
                return HttpResponseRedirect(path + "credit-repair-13")
            else:
                return HttpResponseRedirect(path + "credit-repair-17")


class BusinessEntity(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/businessEntity.html', context=get_context_for_all(request))


class EinView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/ein.html', context=get_context_for_all(request))


class BusinessLicenseView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/businessLicense.html', context=get_context_for_all(request))


class WebsiteCreationOptionsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        profile = Profile.objects.filter(user=request.user)
        website_creation_paid = False
        if profile:
            website_creation_paid = profile[0].website_creation_paid
        if website_creation_paid:
            return redirect(reverse(f"{request.resolver_match.app_name}:website-creation-paid"))
        return redirect(reverse(f"{request.resolver_match.app_name}:website-creation"))
        # return render(request, 'businessCreditBuilding/websiteCreationOptions.html', {'website_creation_paid': website
        # _creation_paid})


class WebsiteCreationPaidView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/websiteCreationPaid.html', context=get_context_for_all(request))


class WebsiteCreationView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/websiteCreation.html', context=get_context_for_all(request))


class FaxNumberOptionsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        profile = Profile.objects.filter(user=request.user)
        fax_number_paid = False
        if profile:
            fax_number_paid = profile[0].fax_number_paid
        if fax_number_paid:
            return redirect(reverse(f"{request.resolver_match.app_name}:fax-number-paid"))
        return redirect(reverse(f"{request.resolver_match.app_name}:fax-number"))
        # return render(request, 'businessCreditBuilding/fa_xNumberOptionsgetcontext_for_all(html', {'fax_number_paid': fax_number_paid}))


class FaxNumberPaidView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/faxNumberPaid.html', context=get_context_for_all(request))


class FaxNumberView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/faxNumber.html', context=get_context_for_all(request))


class FourElevenListingView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/FourElevenListing.html', context=get_context_for_all(request))


class ProfessionalEmailAddress(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/professionalEmailAddress.html',
                      context=get_context_for_all(request))


class DomainView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/domain.html', context=get_context_for_all(request))


class TollFreeNumberOptionsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        profile = Profile.objects.filter(user=request.user)
        toll_free_number_paid = False
        if profile:
            toll_free_number_paid = profile[0].toll_free_number_paid
        if toll_free_number_paid:
            return render(request, 'businessCreditBuilding/tollFreeNumberPaid.html',
                          context=get_context_for_all(request))
            # return redirect(reverse(f"{request.resolver_match.app_name}:toll-free-paid"))

        return render(request, 'businessCreditBuilding/tollFreeNumber.html', context=get_context_for_all(request))
        # return redirect(reverse(f"{request.resolver_match.app_name}:toll-free"))

        # return render(request, 'businessCreditBuilding/tollFreeNumberOptions.html', {'toll_free_number_paid':
        # toll_free_number_paid})


class TollFreeNumberPaidView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/tollFreeNumberPaid.html', context=get_context_for_all(request))


class TollFreeNumberView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/tollFreeNumber.html', context=get_context_for_all(request))


class VirtualAddressView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/virtualAddress.html', context=get_context_for_all(request))


class BusinessBankAccountView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/businessBankAccount.html', context=get_context_for_all(request))


class MerchantAccountView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/merchantAccount.html', context=get_context_for_all(request))


class DunsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/duns.html', context=get_context_for_all(request))


class SICView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/sic.html', context=get_context_for_all(request))


class BusinessGoodStandingView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/businessGoodStanding.html', context=get_context_for_all(request))


class BusinessBackInGoodStandingView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/businessBackInGoodStanding.html',
                      context=get_context_for_all(request))


class BusinessCreditStep(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditStep.html', context=get_context_for_all(request))


class ExperianView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'creditBureaus/experian.html', context=get_context_for_all(request))


class DunnAndBradView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'creditBureaus/dunnbradstreet.html', context=get_context_for_all(request))


class EquifaxView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'creditBureaus/equifax.html', context=get_context_for_all(request))


class StarterVendorListView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        starter_vendors = StarterVendorList.objects.all()
        return render(request, 'cooperateCredit/starter_vendor_list.html',
                      get_context_for_all(request, {"starter_vendors": starter_vendors}))


class StoreCreditVendorListView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        store_credit_vendors = StoreCreditVendorList.objects.all()
        return render(request, "cooperateCredit/store_credit_vendor_list.html",
                      get_context_for_all(request, {"store_credit_vendors": store_credit_vendors}))


class ResolvingBusinessCreditVendorList(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data = [
            {"Name": "Enco Manufacturing Company", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "1"},
            {"Name": "REW Materials", "category": '', "reportTo": 'Equifax Small Business', "link": "2"},
            {"Name": "United Rentals", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "3"},
            {"Name": "Copperfield", "category": '', "reportTo": 'Equifax Small Business', "link": "4"},
        ]
        return render(request, 'cooperateCredit/store_credit_vendor_list.html',
                      get_context_for_all(request, {"list_data": data}))


class LeaderDetailsView(View):
    def get(self, request, state):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, 'cooperateCredit/lender_detail.html', get_context_for_all(data))


class RevolvingBusinessCreditVendorList(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        vendor_list = RevolvingBusinessCreditVendor.objects.all()
        return render(request, 'cooperateCredit/revolving.html',
                      get_context_for_all(request, {"vendor_list": vendor_list}))


class RevolvingDetailsView(View):
    def get(self, request, state):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job \
            easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and \
            maintenance. With reduced fraud and more control, the savings for your business add up. Approval \
            Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting \
            trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, \
            secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. \
            You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing \
            the business address and phone number, and a copy of your business license. (if a business license is \
            required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, 'cooperateCredit/revolving_credit_detail.html', get_context_for_all(data))


class CCNoGuaranteeVendorList(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        nopg_list = Nopg.objects.all()
        return render(request, 'cooperateCredit/nopg.html', get_context_for_all(request, {"nopg_list": nopg_list}))


class NoPgDetailsView(View):
    def get(self, request, state):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, 'cooperateCredit/nopg_detail.html', get_context_for_all(data))


class PersonalCreditCardsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        personal_credit_cards = PersonalCreditCard.objects.all()
        return render(request, "financingProducts/personalCreditCard.html",
                      get_context_for_all(request, {'personal_credit_cards': personal_credit_cards}))


class BusinessCreditCardsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        cc_list = BusinessCreditCard.objects.all()
        return render(request, "financingProducts/businessCreditCard.html",
                      get_context_for_all(request, {"cc_list": cc_list}))


class ShortTermLoans(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        short_term_loans = ShortTermLoan.objects.all()
        return render(request, "financingProducts/shortTermLoans.html",
                      get_context_for_all(request, {'short_term_loans': short_term_loans}))


class BusinessTermLoanView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        business_term_loans = BusinessTermLoan.objects.all()
        return render(request, "financingProducts/businessTermLoan.html",
                      get_context_for_all(request, {'business_term_loans': business_term_loans}))


class SmallBusinessAdminLoanView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        small_business_loans = SbaLoan.objects.all()
        return render(request, "financingProducts/smallBusinessAdminLoan.html",
                      get_context_for_all(request, {'small_business_loans': small_business_loans}))


class PersonalLoanView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        personal_loans = PersonalLoan.objects.all()
        return render(request, "financingProducts/personalLoan.html",
                      get_context_for_all(request, {'personal_loans': personal_loans}))


class BusinessLineOfCredit(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        business_line_credit = LinesOfCredit.objects.all()
        return render(request, "financingProducts/businessLineOfCredit.html",
                      get_context_for_all(request, {'business_line_credit': business_line_credit}))


class NoCreditCheckFinancing(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        loans = NoCreditCheckLoans.objects.all()
        return render(request, "financingProducts/noCreditCheckFinancing.html",
                      context=get_context_for_all(request, {"loans": loans}))


class InvoiceFactoringView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data_list = InvoiceFactoring.objects.all()

        return render(request, "financingProducts/invoiceFactoring.html",
                      context=get_context_for_all(request, {"data_list": data_list}))


class InvoiceFinancingView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data_list = InvoiceFinancing.objects.all()
        return render(request, "financingProducts/invoiceFinancing.html",
                      context=get_context_for_all(request, {"data_list": data_list}))


class EquipmentFinancingView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'immediatemoney/base-immediatemoney.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data_list = EquipmentFinancing.objects.all()
        return render(request, "financingProducts/equipmentFinancing.html",
                      get_context_for_all(request, {"data_list": data_list}))


class MarketingYourBusiness(View):
    def get(self, request):
        return render(request, 'marketingYourBusiness.html', context=get_context_for_all(request))


class OfferFinancingToCustomer(View):
    def get(self, request):
        return render(request, 'customerFinancing.html', context=get_context_for_all(request))


class ApplyingForLoans(View):
    def get(self, request):
        return render(request, 'applyForLoan.html', context=get_context_for_all(request))


class CreditRepairOptionsView(View):
    def get(self, request):
        return render(request, 'creditRepairOptions.html', context=get_context_for_all(request))


class CreditRepairPaidView(View):
    def get(self, request):
        return render(request, 'creditRepairPaid.html', context=get_context_for_all(request))


class CreditRepairView(View):
    def get(self, request):
        return render(request, 'creditRepair.html', context=get_context_for_all(request))


class CreditPrimaryTradeLines(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        data_list = PersonalCreditTradeLine.objects.all()
        return render(request, 'creditPrimaryTradeline.html', get_context_for_all(request, {'data_list': data_list}))


class BusinessCreditRepair(View):
    def get(self, request):
        return render(request, 'businessCreditRepair.html', context=get_context_for_all(request))


class BusinessCreditMonitoringSingUp(View):
    def get(self, request):
        return render(request, 'businessCreditMonitoringSingup.html', context=get_context_for_all(request))


class BusinessCreditCardStrategy(View):
    def get(self, request):
        cc_list = BusinessCreditCard.objects.all()
        return render(request, 'businessCreditCardStrategy.html', get_context_for_all(request, {'cc_list': cc_list}))


class MoneyReferringFriends(View):
    def get(self, request):
        return render(request, 'MoneyReferringFriends.html', context=get_context_for_all(request))


class InsuranceProduct(View):
    def get(self, request):
        return render(request, 'insuranceProduct.html', context=get_context_for_all(request))

class MoneyForBusinessCredit(View):
    def get(self, request):
        return render(request, 'moneyforbusinesscredit.html', context=get_context_for_all(request))


class CreditRepairPlan1View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan1.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan2View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan2.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan3View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan3.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan4View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan4.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan5View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan5.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan6View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan6.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan7View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan7.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan8View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan8.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan9View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan9.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan10View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan10.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan11View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan11.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan12View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan12.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan13View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan13.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan14View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan14.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan15View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan15.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan16View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan16.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan17View(ContextMixin, View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildpersonalcredit/base-buildpersonalcredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, "creditrepair/creditrepairplan17.html",
                      context=get_context_for_all(request, self.get_context_data()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class VirtualCardView(View):
    def get(self, request):
        card = request.user.virtual_card
        return render(request, "home/virtualcard.html", get_context_for_all(request, {"virtual_card": card}))


class BusinessStepsMobile(View):
    def get(self, request):
        return render(request, "userData/BusinessCreditSteps_mobile.html")
