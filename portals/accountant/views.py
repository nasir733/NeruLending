from django.shortcuts import render, redirect
from business.models import (
    Profile, Lender, StoreCreditVendorList, RevolvingCredit, Nopg, ShortTermLoan, BusinessTermLoan, SbaLoan,
    LinesOfCredit, StarterVendorList, PersonalCreditCard, PersonalLoan, RevolvingBusinessCreditVendor,
    BusinessCreditCard, EquipmentFinancing, PersonalCreditTradeLine
)
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.base import ContextMixin

app_name = 'accountant'


def get_business_plan_context():
    lenders = Lender.objects.all()
    store_credits = StoreCreditVendorList.objects.all()
    revolvings = RevolvingCredit.objects.all()
    nopgs = Nopg.objects.all()
    context = {
        "lenders": lenders,
        "store_credits": store_credits,
        "revolvings": revolvings,
        "nopgs": nopgs
    }

    return context


class BusinessHomePage(View):
    def get(self, request):
        return render(request, f"{app_name}/index-accountant.html")


class BusinessPlan1View(View):
    def get(self, request):
        return render(request, f"{app_name}/home/businessplan1.html", context=get_business_plan_context())


class BusinessPlan2View(View):
    def get(self, request):
        return render(request, f"{app_name}/home/businessplan2.html", context=get_business_plan_context())


class BusinessPlan3View(View):
    def get(self, request):
        return render(request, f"{app_name}/home/businessplan3.html", context=get_business_plan_context())


class BusinessCreditBuildingPlanView(View):
    def get(self, request):
        return render(request, f"{app_name}/home/business.html")

    def post(self, request):
        data = request.POST
        business_time = int(data['business_time'])
        trade_lines = int(data['trade_lines'])
        if business_time == 1:
            if trade_lines == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_1"))
            elif trade_lines == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_3"))
        elif business_time == 2:
            if trade_lines == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_1"))
            elif trade_lines == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_3"))
        elif business_time == 3:
            if trade_lines == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_1"))
            elif trade_lines == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(reverse(f"{app_name}:business_plan_3"))


class UpgradeView(View):
    def get(self, request):
        return render(request, f"{app_name}/home/upgrade.html")


class FinancingView(View):
    def get(self, request):
        return render(request, f"{app_name}/financing.html")

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

        if experian == 1:
            if monthly_revenue_3 == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_8"))
            else:
                if business_age == 5:
                    return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_12"))
                else:
                    return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_1"))
        if experian == 2:
            if monthly_revenue_3 == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_7"))
            elif monthly_revenue_3 == 2:
                if business_age == 5:
                    return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_15"))
            else:
                return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_2"))

        if experian == 3:
            if monthly_revenue_3 == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_6"))
            else:
                if business_age <= 4:
                    return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_3"))
                else:
                    return HttpResponseRedirect(reverse(f"{app_name}:financing_plan_10"))


class FinancingPlan1View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/financingplans/financingplan1.html", context=self.get_context_data())

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
        return render(request, f"{app_name}/financingplans/financingplan2.html", context=self.get_context_data())

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
        return render(request, f"{app_name}/financingplans/financingplan3.html", context=self.get_context_data())

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
        return render(request, f"{app_name}/financingplans/financingplan6.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenders'] = []
        context['equipments'] = []
        return context


class FinancingPlan7View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/financingplans/financingplan7.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenders'] = []
        context['invoices'] = []
        context['equipments'] = []
        return context


class FinancingPlan8View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/financingplans/financingplan8.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenders'] = []
        context['equipments'] = []
        return context


class FinancingPlan10View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/financingplans/financingplan10.html", context=self.get_context_data())

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
        return render(request, f"{app_name}/financingplans/financingplan12.html", context=self.get_context_data())

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
        return render(request, f"{app_name}/financingplans/financingplan15.html", context=self.get_context_data())

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
        return render(request, f"{app_name}/home/creditsituation.html")

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

        if experian_score == 1:
            if bankruptcies_10 == 1:
                if credit_history_experian == 1:
                    return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_1"))
                else:
                    # a tie btn 4 and 7
                    return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_7"))
            if inquiries == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_14"))
            else:
                if missed_payments == 1:
                    return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_8"))
                else:
                    return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_11"))
        elif experian_score == 2:
            if bankruptcies_10 == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_5"))
            if inquiries == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_15"))
            if missed_payments == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_9"))
            if missed_payments == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_12"))
            else:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_17"))

        else:
            if bankruptcies_10 == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_6"))
            if inquiries == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_16"))
            if missed_payments == 1:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_10"))
            if missed_payments == 2:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_13"))
            else:
                return HttpResponseRedirect(reverse(f"{app_name}:credit_repair_17"))

class BusinessEntity(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/businessEntity.html")


class EinView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/ein.html")


class BusinessLicenseView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/businessLicense.html")


class WebsiteCreationOptionsView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        website_creation_paid = False
        if profile:
            website_creation_paid = profile[0].website_creation_paid
        if website_creation_paid:
            return redirect(reverse(f'{app_name}:website-creation-paid'))
        return redirect(reverse(f'{app_name}:website-creation'))
        # return render(request, 'businessCreditBuilding/websiteCreationOptions.html', {'website_creation_paid': website
        # _creation_paid})


class WebsiteCreationPaidView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/websiteCreationPaid.html")


class WebsiteCreationView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/websiteCreation.html")


class FaxNumberOptionsView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        fax_number_paid = False
        if profile:
            fax_number_paid = profile[0].fax_number_paid
        if fax_number_paid:
            return redirect(reverse(f'{app_name}:fax-number-paid'))
        return redirect(reverse(f'{app_name}:fax-number'))
        # return render(request, 'businessCreditBuilding/faxNumberOptions.html', {'fax_number_paid': fax_number_paid})


class FaxNumberPaidView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/faxNumberPaid.html")


class FaxNumberView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/faxNumber.html")


class FourElevenListingView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/FourElevenListing.html")


class ProfessionalEmailAddress(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/professionalEmailAddress.html")


class DomainView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/domain.html")


class TollFreeNumberOptionsView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        toll_free_number_paid = False
        if profile:
            toll_free_number_paid = profile[0].toll_free_number_paid
        if toll_free_number_paid:
            return redirect(reverse(f'{app_name}:toll-free-paid'))
        return redirect(reverse(f'{app_name}:toll-free'))
        # return render(request, 'businessCreditBuilding/tollFreeNumberOptions.html', {'toll_free_number_paid':
        # toll_free_number_paid})


class TollFreeNumberPaidView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/tollFreeNumberPaid.html")


class TollFreeNumberView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/tollFreeNumber.html")


class VirtualAddressView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/virtualAddress.html")


class BusinessBankAccountView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/businessBankAccount.html")


class MerchantAccountView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/merchantAccount.html")


class DunsView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/duns.html")


class SICView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/sic.html")


class BusinessGoodStandingView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/businessGoodStanding.html")


class BusinessBackInGoodStandingView(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditBuilding/businessBackInGoodStanding.html")


class BusinessCreditStep(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditStep.html")


class ExperianView(View):
    def get(self, request):
        return render(request, f"{app_name}/creditBureaus/experian.html")


class DunnAndBradView(View):
    def get(self, request):
        return render(request, f"{app_name}/creditBureaus/dunnbradstreet.html")


class EquifaxView(View):
    def get(self, request):
        return render(request, f"{app_name}/creditBureaus/equifax.html")


class StarterVendorListView(View):
    def get(self, request):
        starter_vendors = StarterVendorList.objects.all()
        return render(request, f"{app_name}/cooperateCredit/starter_vendor_list.html", {"starter_vendors": starter_vendors})


class StoreCreditVendorListView(View):
    def get(self, request):
        store_credit_vendors = StoreCreditVendorList.objects.all()
        return render(request, f"{app_name}/cooperateCredit/store_credit_vendor_list.html",
                      {"store_credit_vendors": store_credit_vendors})


class ResolvingBusinessCreditVendorList(View):
    def get(self, request):
        data = [
            {"Name": "Enco Manufacturing Company", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "1"},
            {"Name": "REW Materials", "category": '', "reportTo": 'Equifax Small Business', "link": "2"},
            {"Name": "United Rentals", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "3"},
            {"Name": "Copperfield", "category": '', "reportTo": 'Equifax Small Business', "link": "4"},
        ]
        return render(request, f"{app_name}/cooperateCredit/store_credit_vendor_list.html", {"list_data": data})


class LeaderDetailsView(View):
    def get(self, request, state):
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, f"{app_name}/cooperateCredit/lender_detail.html", data)


class RevolvingBusinessCreditVendorList(View):
    def get(self, request):
        vendor_list = RevolvingBusinessCreditVendor.objects.all()
        return render(request, f"{app_name}/cooperateCredit/revolving.html", {"vendor_list": vendor_list})


class RevolvingDetailsView(View):
    def get(self, request, state):
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
        return render(request, f"{app_name}/cooperateCredit/revolving_credit_detail.html", data)


class CCNoGuaranteeVendorList(View):
    def get(self, request):
        nopg_list = Nopg.objects.all()
        return render(request, f"{app_name}/cooperateCredit/nopg.html", {"nopg_list": nopg_list})


class NoPgDetailsView(View):
    def get(self, request, state):
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, f"{app_name}/cooperateCredit/nopg_detail.html", data)


class PersonalCreditCardsView(View):
    def get(self, request):
        personal_credit_cards = PersonalCreditCard.objects.all()
        return render(request, f"{app_name}/financingProducts/personalCreditCard.html", {'personal_credit_cards': personal_credit_cards})


class BusinessCreditCardsView(View):
    def get(self, request):
        cc_list = BusinessCreditCard.objects.all()
        return render(request, f"{app_name}/home/businesscards.html", {"cc_list": cc_list})


class ShortTermLoans(View):
    def get(self, request):
        short_term_loans = ShortTermLoan.objects.all()
        return render(request, f"{app_name}/financingProducts/shortTerm.html", {'short_term_loans': short_term_loans})


class BusinessTermLoanView(View):
    def get(self, request):
        business_term_loans = BusinessTermLoan.objects.all()
        return render(request, f"{app_name}/financingProducts/businessTermLoan.html", {'business_term_loans': business_term_loans})


class SmallBusinessAdminLoanView(View):
    def get(self, request):
        small_business_loans = SbaLoan.objects.all()
        return render(request, f"{app_name}/financingProducts/smallBusinessAdminLoan.html",
                      {'small_business_loans': small_business_loans})


class PersonalLoanView(View):
    def get(self, request):
        personal_loans = PersonalLoan.objects.all()
        return render(request, f"{app_name}/financingProducts/personalLoan.html", {'personal_loans': personal_loans})


class BusinessLineOfCredit(View):
    def get(self, request):
        business_line_credit = LinesOfCredit.objects.all()
        return render(request, f"{app_name}/financingProducts/businessLineOfCredit.html",
                      {'business_line_credit': business_line_credit})


class NoCreditCheckFinancing(View):
    def get(self, request):
        return render(request, f"{app_name}/financingProducts/noCreditCheckFinancing.html")


class InvoiceFactoring(View):
    def get(self, request):
        return render(request, f"{app_name}/financingProducts/invoiceFactoring.html")


class InvoiceFinancing(View):
    def get(self, request):
        return render(request, f"{app_name}/financingProducts/invoiceFinancing.html")


class EquipmentFinancingView(View):
    def get(self, request):
        data_list = EquipmentFinancing.objects.all()
        return render(request, f"{app_name}/financingProducts/equipmentFinancing.html", {"data_list": data_list})


class MarketingYourBusiness(View):
    def get(self, request):
        return render(request, f"{app_name}/marketingYourBusiness.html")


class OfferFinancingToCustomer(View):
    def get(self, request):
        return render(request, f"{app_name}/customerFinancing.html")


class ApplyingForLoans(View):
    def get(self, request):
        return render(request, f"{app_name}/applyforLoan.html")


class CreditRepairOptionsView(View):
    def get(self, request):
        return render(request, f"{app_name}/creditRepairOptions.html")


class CreditRepairPaidView(View):
    def get(self, request):
        return render(request, f"{app_name}/creditRepairPaid.html")


class CreditRepairView(View):
    def get(self, request):
        return render(request, f"{app_name}/creditRepair.html")


class CreditPrimaryTradeLines(View):
    def get(self, request):
        data_list = PersonalCreditTradeLine.objects.all()
        return render(request, f"{app_name}/creditPrimaryTradeline.html", {'data_list': data_list})


class BusinessCreditRepair(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditRepair.html")


class BusinessCreditMonitoringSingUp(View):
    def get(self, request):
        return render(request, f"{app_name}/businessCreditMonitoringSingup.html")


class BusinessCreditCardStrategy(View):
    def get(self, request):
        cc_list = BusinessCreditCard.objects.all()
        return render(request, f"{app_name}/businessCreditCardStrategy.html", {'cc_list': cc_list})


class MoneyReferringFriends(View):
    def get(self, request):
        return render(request, f"{app_name}/MoneyReferringFriends.html")


class InsuranceProduct(View):
    def get(self, request):
        return render(request, f"{app_name}/insuranceProduct.html")


class CreditRepairPlan1View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan1.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan2View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan2.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan3View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan3.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan4View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan4.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan5View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan5.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan6View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan6.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan7View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan7.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan8View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan8.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan9View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan9.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan10View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan10.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan11View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan11.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan12View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan12.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan13View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan13.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan14View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan14.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan15View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan15.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan16View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan16.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context


class CreditRepairPlan17View(ContextMixin, View):
    def get(self, request):
        return render(request, f"{app_name}/creditrepair/creditrepairplan17.html", context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shortterm'] = []
        return context
