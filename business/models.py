from django.db import models
from django.utils import timezone
from user.models import Profile


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    @property
    def get_url(self):
        if hasattr(self, 'url'):
            if not self.url.startswith("http"):
                return "http://" + self.url
            else:
                return self.url


class BusinessCreditSteps(ModelMixin, models.Model):
    class Meta:
        verbose_name = "Business Credit steps"
        verbose_name_plural = "Business Credit steps"

    choices = (
        ("1", "Dentist"),
        ("2", "Real Estate"),
        ("3", "Restaurant"),
        ("4", "Auto Repair"),
        ("5", "Trucking"),
        ("6", "Hair Salon"),
        ("7", "Transportation Services"),
        ("8", "Electrician"),
        ("9", "Lawyer"),
        ("10", "Photography"),
        ("11", "Landscaping"),
        ("12", "Musician"),
        ("13", "Ecommece"),
        ("14", "Insurance Agent"),
        ("15", "Accountant"),
        ("16", "Carpet & Flooring"),
        ("17", "Barber"),
        ("18", "Spa"),
        ("19", "Wedding Planner"),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=5000, null=True)
    last_name = models.CharField(max_length=5000, null=True)
    email = models.CharField(max_length=5000, null=True)
    phone = models.CharField(max_length=5000, null=True)

    website = models.BooleanField(default=False)
    fax = models.BooleanField(default=False)
    toll_free_number = models.BooleanField(default=False)
    domain = models.BooleanField(default=False)
    pro_email_address = models.BooleanField(default=False)

    website_inndustry = models.CharField(max_length=5000, null=True, blank=True, choices=choices)


class FinancingInformation(ModelMixin, models.Model):
    class Meta:
        db_table = 'financing_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experian = models.CharField(max_length=5000)
    equifax = models.CharField(max_length=5000)
    transunion = models.CharField(max_length=5000)
    monthly_revenue_3 = models.CharField(max_length=5000)
    daily_balance_3 = models.CharField(max_length=5000)
    monthlty_ending_balance_3 = models.CharField(max_length=5000)
    monthly_revenue_6 = models.CharField(max_length=5000)
    daily_balance_6 = models.CharField(max_length=5000)
    monthlty_ending_balance_6 = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    nonsufficient_6 = models.CharField(max_length=5000)
    nonsufficient_12 = models.CharField(max_length=5000)
    current_liens = models.CharField(max_length=5000)
    business_account = models.CharField(max_length=5000)
    business_loan = models.CharField(max_length=5000)
    business_age = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class CreditRepairInformation(ModelMixin, models.Model):
    class Meta:
        db_table = 'credit_repair_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experian_score = models.CharField(max_length=5000)
    equifax_score = models.CharField(max_length=5000)
    transunion_score = models.CharField(max_length=5000)
    experian_utilization = models.CharField(max_length=5000)
    equifax_utilization = models.CharField(max_length=5000)
    transunion_utilization = models.CharField(max_length=5000)
    current_collections = models.CharField(max_length=5000)
    bankruptcies = models.CharField(max_length=5000)
    bankruptcies_10 = models.CharField(max_length=5000)
    inquiries = models.CharField(max_length=5000)
    missed_payments = models.CharField(max_length=5000)
    current_acc_experian = models.CharField(max_length=5000)
    current_acc_equifax = models.CharField(max_length=5000)
    current_acc_transunion = models.CharField(max_length=5000)
    credit_history_experian = models.CharField(max_length=5000)
    credit_history_equifax = models.CharField(max_length=5000)
    credit_history_transunion = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class BusinessCreditInformation(ModelMixin, models.Model):
    class Meta:
        db_table = 'businesscredit_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_time = models.CharField(max_length=5000, null=True)
    trade_lines = models.CharField(max_length=5000, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Domain(ModelMixin, models.Model):
    class Meta:
        db_table = 'domain'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=5000)
    domain_needed = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class FinancingPlanRegularPerson(ModelMixin, models.Model):
    class Meta:
        db_table = 'financingplanregularperson'

    name = models.CharField(max_length=5000, null=True)
    description = models.CharField(max_length=5500, null=True)
    report_to = models.CharField(max_length=5000, null=True)
    monthly_payment = models.CharField(max_length=5000, null=True)
    estimated_term = models.CharField(max_length=5000, null=True)
    estimated_amount = models.CharField(max_length=5000, null=True)
    payment_terms = models.CharField(max_length=5000, null=True)
    terms = models.CharField(max_length=5000, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class EquipmentFinancing(ModelMixin, models.Model):
    class Meta:
        db_table = 'equipment_financing'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Fax(ModelMixin, models.Model):
    class Meta:
        db_table = 'fax'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fax_needed = models.CharField(max_length=5000)
    created_at = models.CharField(max_length=5000)
    updated_at = models.DateTimeField(null=True, blank=True)


class InvoiceFactoring(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoice_factoring'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class InvoiceFinancing(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoice_financing'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Category(models.Model):
    class Meta:
        db_table = 'category'

    title = models.CharField(max_length=5000)


class Lender(ModelMixin, models.Model):
    class Meta:
        db_table = 'lender'

    name = models.CharField(max_length=5000, null=True)
    description = models.CharField(max_length=5000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    report_to = models.CharField(max_length=5000, null=True)
    monthly_payment = models.CharField(max_length=5000, null=True)
    estimated_term = models.CharField(max_length=5000, null=True)
    estimated_amount = models.CharField(max_length=5000, null=True)
    payment_terms = models.CharField(max_length=5000, null=True)
    terms = models.CharField(max_length=5000, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class LinesOfCredit(ModelMixin, models.Model):
    class Meta:
        db_table = 'lines_of_credit'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Nopg(ModelMixin, models.Model):
    class Meta:
        db_table = 'nopg'

    name = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    reports_to = models.CharField(max_length=5000)
    estimated_amount = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProfessionalEmailAddress(ModelMixin, models.Model):
    class Meta:
        db_table = 'professional_email_address'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email_address_needed = models.CharField(max_length=5000)
    domain_present = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Progress(ModelMixin, models.Model):
    class Meta:
        db_table = 'progress'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website_creation = models.CharField(max_length=5000)
    dns_number = models.CharField(max_length=5000)
    virtual_number = models.CharField(max_length=5000)
    fax_number = models.CharField(max_length=5000)
    toll_free_number = models.CharField(max_length=5000)
    business_bank_account = models.CharField(max_length=5000)
    listing = models.CharField(max_length=5000)
    professional_email_address = models.CharField(max_length=5000)
    domain = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Industry(models.Model):
    class Meta:
        db_table = 'industry'

    title = models.CharField(max_length=5000)


class RevenueLending(ModelMixin, models.Model):
    class Meta:
        db_table = 'revenue_lending'

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fico_score = models.CharField(max_length=5000)
    equifax_score = models.CharField(max_length=5000)
    transunion_score = models.CharField(max_length=5000)
    avg_monthly_revenue = models.CharField(max_length=5000)
    abg_daily_balance = models.CharField(max_length=5000)
    avg_monthly_ending_balance = models.CharField(max_length=5000)
    business_debt = models.CharField(max_length=5000)
    liens = models.CharField(max_length=5000)
    business_bank_account = models.CharField(max_length=5000)
    age = models.IntegerField()
    registered_at = models.DateTimeField(null=True, blank=True)
    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class RevolvingCredit(ModelMixin, models.Model):
    class Meta:
        db_table = 'revolving_credit'

    name = models.CharField(max_length=5000)
    report_to = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class SbaLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'sba_loan'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class ShortTermLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'short_term_loan'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class BusinessTermLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'term_loan'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class StoreCreditVendorList(ModelMixin, models.Model):
    class Meta:
        db_table = 'store_credit_vendor_2'

    name = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    reports_to = models.CharField(max_length=5000)
    estimated_amount = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class StarterVendorList(ModelMixin, models.Model):
    class Meta:
        db_table = 'starter_vendor_list'

    name = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    report_to = models.CharField(max_length=5000)
    monthly_payment = models.CharField(max_length=5000)
    estimated_terms = models.CharField(max_length=5000)
    estimated_amount = models.CharField(max_length=5000)
    payment_terms = models.CharField(max_length=5000)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class TollFreeNumber(ModelMixin, models.Model):
    class Meta:
        db_table = 'toll_free_number'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    toll_free_number_needed = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class WebsiteCreation(ModelMixin, models.Model):
    class Meta:
        db_table = 'website_creation'

    industry_name = models.CharField(max_length=5000)
    booking_on_page = models.CharField(max_length=5000)
    business_name = models.CharField(max_length=5000)
    chat_bot = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    theme = models.CharField(max_length=5000)
    pages_needed = models.CharField(max_length=5000)
    services = models.CharField(max_length=5000)
    domain = models.CharField(max_length=5000)
    about_you = models.CharField(max_length=5500)
    url = models.CharField(max_length=5000)
    domain_owned = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class PersonalCreditCard(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_credit_card'

    cc_name = models.CharField(max_length=5000)
    min_credit_score = models.CharField(max_length=5000)
    credit_bureau = models.CharField(max_length=5000)
    debt_ratio = models.CharField(max_length=5000)
    bankruptcy = models.CharField(max_length=5000)
    credit_data = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    misc_info = models.CharField(max_length=5000)
    url = models.CharField(blank=True, max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.cc_name


class BusinessCreditCard(ModelMixin, models.Model):
    class Meta:
        db_table = 'business_credit_card'

    cc_name = models.CharField(null=True, max_length=5000)
    min_credit_score = models.CharField(null=True, max_length=5000)
    credit_bureau = models.CharField(null=True, max_length=5000)
    debt_ratio = models.CharField(null=True, max_length=5000)
    bankruptcy = models.CharField(null=True, max_length=5000)
    credit_data = models.CharField(null=True, max_length=5000)
    apr = models.CharField(null=True, max_length=5000)
    strategy = models.CharField(null=True, max_length=5000)
    max_inquiries = models.CharField(null=True, max_length=5000)
    url = models.CharField(blank=True, max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.cc_name


class PersonalLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_loan'

    lender_name = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    inquiries = models.CharField(max_length=5000)
    credit_bureau = models.CharField(max_length=5000)
    states = models.CharField(max_length=5000)
    credit_score = models.CharField(max_length=5000)
    emp_length = models.CharField(max_length=5000)
    credit_history = models.CharField(max_length=5000)
    url = models.CharField(blank=True, max_length=5000)

    def __str__(self):
        return self.lender_name


class RevolvingBusinessCreditVendor(ModelMixin, models.Model):
    class Meta:
        db_table = 'revolving_business_credit'

    name = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=5000)
    url = models.CharField(blank=True, max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class NoCreditCheckLoans(ModelMixin, models.Model):
    class Meta:
        db_table = 'nocreditcheck_loans'

    lender_name = models.CharField(null=True, max_length=5000)
    estimated_terms = models.CharField(null=True, max_length=5000)
    url = models.CharField(null=True, max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class PersonalCreditTradeLine(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_credit_tradeline'

    lender_name = models.CharField(max_length=5000)
    hard_check = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)
    url = models.CharField(max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
