from django.db import models
from django.utils import timezone
from user.models import Profile


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class FinancingInformation(ModelMixin, models.Model):
    class Meta:
        db_table = 'financing_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experian = models.CharField(max_length=500)
    equifax = models.CharField(max_length=500)
    transunion = models.CharField(max_length=500)
    monthly_revenue_3 = models.CharField(max_length=500)
    daily_balance_3 = models.CharField(max_length=500)
    monthlty_ending_balance_3 = models.CharField(max_length=500)
    monthly_revenue_6 = models.CharField(max_length=500)
    daily_balance_6 = models.CharField(max_length=500)
    monthlty_ending_balance_6 = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    nonsufficient_6 = models.CharField(max_length=500)
    nonsufficient_12 = models.CharField(max_length=500)
    current_liens = models.CharField(max_length=500)
    business_account = models.CharField(max_length=500)
    business_loan = models.CharField(max_length=500)
    business_age = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class CreditRepairInformation(ModelMixin, models.Model):
    class Meta:
        db_table = 'credit_repair_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experian_score = models.CharField(max_length=500)
    equifax_score = models.CharField(max_length=500)
    transunion_score = models.CharField(max_length=500)
    experian_utilization = models.CharField(max_length=500)
    equifax_utilization = models.CharField(max_length=500)
    transunion_utilization = models.CharField(max_length=500)
    current_collections = models.CharField(max_length=500)
    bankruptcies = models.CharField(max_length=500)
    bankruptcies_10 = models.CharField(max_length=500)
    inquiries = models.CharField(max_length=500)
    missed_payments = models.CharField(max_length=500)
    current_acc_experian = models.CharField(max_length=500)
    current_acc_equifax = models.CharField(max_length=500)
    current_acc_transunion = models.CharField(max_length=500)
    credit_history_experian = models.CharField(max_length=500)
    credit_history_equifax = models.CharField(max_length=500)
    credit_history_transunion = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class BusinessCreditInformation(ModelMixin, models.Model):
    class Meta:
        db_table = 'businesscredit_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_time = models.CharField(max_length=500, null=True)
    trade_lines = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Domain(ModelMixin, models.Model):
    class Meta:
        db_table = 'domain'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=500)
    domain_needed = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class FinancingPlanRegularPerson(ModelMixin, models.Model):
    class Meta:
        db_table = 'financingplanregularperson'

    name = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=5000, null=True)
    report_to = models.CharField(max_length=500, null=True)
    monthly_payment = models.CharField(max_length=15, null=True)
    estimated_term = models.CharField(max_length=500, null=True)
    estimated_amount = models.CharField(max_length=5, null=True)
    payment_terms = models.CharField(max_length=500, null=True)
    terms = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class EquipmentFinancing(ModelMixin, models.Model):
    class Meta:
        db_table = 'equipment_financing'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Fax(ModelMixin, models.Model):
    class Meta:
        db_table = 'fax'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fax_needed = models.CharField(max_length=500)
    created_at = models.CharField(max_length=500)
    updated_at = models.DateTimeField(null=True, blank=True)


class InvoiceFactoring(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoice_factoring'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class InvoiceFinancing(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoice_financing'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Category(models.Model):
    class Meta:
        db_table = 'category'

    title = models.CharField(max_length=500)


class Lender(ModelMixin, models.Model):
    class Meta:
        db_table = 'lender'

    name = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=5000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    report_to = models.CharField(max_length=500, null=True)
    monthly_payment = models.CharField(max_length=15, null=True)
    estimated_term = models.CharField(max_length=500, null=True)
    estimated_amount = models.CharField(max_length=5, null=True)
    payment_terms = models.CharField(max_length=500, null=True)
    terms = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class LinesOfCredit(ModelMixin, models.Model):
    class Meta:
        db_table = 'lines_of_credit'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Nopg(ModelMixin, models.Model):
    class Meta:
        db_table = 'nopg'

    name = models.CharField(max_length=200)
    terms = models.CharField(max_length=200)
    reports_to = models.CharField(max_length=200)
    estimated_amount = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProfessionalEmailAddress(ModelMixin, models.Model):
    class Meta:
        db_table = 'professional_email_address'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email_address_needed = models.CharField(max_length=500)
    domain_present = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Progress(ModelMixin, models.Model):
    class Meta:
        db_table = 'progress'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website_creation = models.CharField(max_length=500)
    dns_number = models.CharField(max_length=500)
    virtual_number = models.CharField(max_length=500)
    fax_number = models.CharField(max_length=500)
    toll_free_number = models.CharField(max_length=500)
    business_bank_account = models.CharField(max_length=500)
    listing = models.CharField(max_length=500)
    professional_email_address = models.CharField(max_length=500)
    domain = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Industry(models.Model):
    class Meta:
        db_table = 'industry'

    title = models.CharField(max_length=500)


class RevenueLending(ModelMixin, models.Model):
    class Meta:
        db_table = 'revenue_lending'

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fico_score = models.CharField(max_length=500)
    equifax_score = models.CharField(max_length=500)
    transunion_score = models.CharField(max_length=500)
    avg_monthly_revenue = models.CharField(max_length=500)
    abg_daily_balance = models.CharField(max_length=500)
    avg_monthly_ending_balance = models.CharField(max_length=500)
    business_debt = models.CharField(max_length=500)
    liens = models.CharField(max_length=500)
    business_bank_account = models.CharField(max_length=500)
    age = models.IntegerField()
    registered_at = models.DateTimeField(null=True, blank=True)
    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class RevolvingCredit(ModelMixin, models.Model):
    class Meta:
        db_table = 'revolving_credit'

    name = models.CharField(max_length=200)
    report_to = models.CharField(max_length=200)
    terms = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class SbaLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'sba_loan'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class ShortTermLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'short_term_loan'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class BusinessTermLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'term_loan'

    lender_name = models.CharField(max_length=500)
    personal_credit_score = models.CharField(max_length=500)
    time_in_business = models.CharField(max_length=500)
    business_revenue = models.CharField(max_length=500)
    term_length = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class StoreCreditVendorList(ModelMixin, models.Model):
    class Meta:
        db_table = 'store_credit_vendor_2'

    name = models.CharField(max_length=200)
    terms = models.CharField(max_length=200)
    reports_to = models.CharField(max_length=200)
    estimated_amount = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class StarterVendorList(ModelMixin, models.Model):
    class Meta:
        db_table = 'starter_vendor_list'

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    terms = models.CharField(max_length=500)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=500)
    url = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class TollFreeNumber(ModelMixin, models.Model):
    class Meta:
        db_table = 'toll_free_number'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    toll_free_number_needed = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class WebsiteCreation(ModelMixin, models.Model):
    class Meta:
        db_table = 'website_creation'

    industry_name = models.CharField(max_length=500)
    booking_on_page = models.CharField(max_length=500)
    business_name = models.CharField(max_length=500)
    chat_bot = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    theme = models.CharField(max_length=500)
    pages_needed = models.CharField(max_length=500)
    services = models.CharField(max_length=500)
    domain = models.CharField(max_length=500)
    about_you = models.CharField(max_length=5000)
    url = models.CharField(max_length=200)
    domain_owned = models.CharField(max_length=500)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class PersonalCreditCard(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_credit_card'

    cc_name = models.CharField(max_length=500)
    min_credit_score = models.CharField(max_length=500)
    credit_bureau = models.CharField(max_length=500)
    debt_ratio = models.CharField(max_length=500)
    bankruptcy = models.CharField(max_length=500)
    credit_data = models.CharField(max_length=500)
    apr = models.CharField(max_length=500)
    misc_info = models.CharField(max_length=500)
    url = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.cc_name


class BusinessCreditCard(ModelMixin, models.Model):
    class Meta:
        db_table = 'business_credit_card'

    cc_name = models.CharField(null=True, max_length=500)
    min_credit_score = models.CharField(null=True, max_length=500)
    credit_bureau = models.CharField(null=True, max_length=500)
    debt_ratio = models.CharField(null=True, max_length=500)
    bankruptcy = models.CharField(null=True, max_length=500)
    credit_data = models.CharField(null=True, max_length=500)
    apr = models.CharField(null=True, max_length=500)
    strategy = models.CharField(null=True, max_length=500)
    max_inquiries = models.CharField(null=True, max_length=500)
    url = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.cc_name


class PersonalLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_loan'

    lender_name = models.CharField(max_length=500)
    terms = models.CharField(max_length=500)
    inquiries = models.CharField(max_length=500)
    credit_bureau = models.CharField(max_length=500)
    states = models.CharField(max_length=500)
    credit_score = models.CharField(max_length=500)
    emp_length = models.CharField(max_length=500)
    credit_history = models.CharField(max_length=500)
    url = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.lender_name


class RevolvingBusinessCreditVendor(ModelMixin, models.Model):
    class Meta:
        db_table = 'revolving_business_credit'

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    terms = models.CharField(max_length=500)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=500)
    url = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class NoCreditCheckLoans(ModelMixin, models.Model):
    class Meta:
        db_table = 'nocreditcheck_loans'

    lender_name = models.CharField(null=True, max_length=500)
    estimated_terms = models.CharField(null=True, max_length=200)
    url = models.CharField(null=True, max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class PersonalCreditTradeLine(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_credit_tradeline'

    lender_name = models.CharField(max_length=500)
    hard_check = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
