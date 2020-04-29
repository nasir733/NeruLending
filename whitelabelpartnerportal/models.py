from django.db import models
from user.models import Profile
from django.utils import timezone


app_name = 'whitelabelpartnerportal'


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Residual(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_residual'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    amountofresiduals = models.CharField(max_length=50, null=True)
    product = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()

class BecomingAPartner(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_becomingapartner'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    business_name = models.CharField(max_length=50, null=True)
    business_number = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Lead(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_lead'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    business_name = models.CharField(max_length=100, null=True)
    business_package = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class AffiliateAgents(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_affiliate_agents'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    full_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Sale(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_sale'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    sales = models.CharField(max_length=50, null=True)
    product = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class AffiliateResidual(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_affiliate_residual'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    amount = models.CharField(max_length=50, null=True)
    affiliate_name = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Credit(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_credit'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    account_name = models.CharField(max_length=50, null=True)
    created = models.CharField(max_length=50, null=True, default='')
    applied = models.CharField(max_length=50, null=True, default='')
    amount = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class FreeProgram(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_free_program'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    client_name = models.CharField(max_length=50, null=True)
    client_email = models.CharField(max_length=50, null=True)
    client_phone_number = models.CharField(max_length=50, null=True)
    updates_made = models.CharField(max_length=500, null=True)
    residual_amount = models.CharField(max_length=500, null=True)
    expected_payout = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class PaidProgram(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_paid_program'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    client_name = models.CharField(max_length=50, null=True)
    client_email = models.CharField(max_length=50, null=True)
    client_phone_number = models.CharField(max_length=50, null=True)
    updates_made = models.CharField(max_length=500, null=True)
    residual_amount = models.CharField(max_length=500, null=True)
    expected_payout = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Invoice(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_invoice'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    product = models.CharField(max_length=50, null=True)
    invoiceamount = models.CharField(max_length=50, null=True)
    invoiceduedate = models.DateTimeField(null=True)
    status = models.CharField(max_length=500, null=True)
    paynow = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Order(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_order'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    order_placed = models.CharField(max_length=50, null=True)
    date_ordered = models.DateTimeField(null=True)
    order_amount = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Payment(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_payments'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    payment = models.CharField(max_length=50, null=True)
    account_name = models.CharField(max_length=500, null=True)
    amount_paid = models.CharField(max_length=500, null=True)
    date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class BankPaymentInformation(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_bank_payment_information'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    routing_number = models.CharField(max_length=500, null=True)
    name_of_bank = models.CharField(max_length=500, null=True)
    account_number = models.CharField(max_length=500, null=True)
    name_on_bank_account = models.CharField(max_length=500, null=True)
    your_address = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class PaypalInformation(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_paypal_information'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    paypal_email = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class WhitelabelWebsite(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_whitelabel_website'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    website_name = models.CharField(max_length=500, null=True)
    website_link = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class WhitelabelPortal(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_whitelabel_portal'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    free_portal = models.CharField(max_length=500, null=True, default='')
    paid_portal = models.CharField(max_length=500, null=True, default='')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class WhitelabelBusinessPackage(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_whitelabel_business_package'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    website_login = models.CharField(max_length=500, null=True)
    toll_free_number_login = models.CharField(max_length=500, null=True)
    professional_email_address_login = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Webinar(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_webinars'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    link = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()
