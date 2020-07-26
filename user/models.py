import stripe
from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProfileUserManager(models.Manager):
    def create_user(self, email, password, first_name, last_name, phone_number):
        stripe_user = stripe.Customer.create(
            name=f"{first_name} {last_name}",
            email=email
        )

        user = User.objects.create_user(email=email, username=email, password=password, first_name=first_name,
                                        last_name=last_name)
        profile = Profile(user=user, phone_number=phone_number, stripe_id=stripe_user['id'])
        profile.save()
        return profile


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15)
    fax_number_paid = models.BooleanField(default=False)
    toll_free_number_paid = models.BooleanField(default=False)
    website_creation_paid = models.BooleanField(default=False)
    virtual_access_card_paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=200, null=True)
    objects = ProfileUserManager()

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

    class Meta:
        verbose_name = "1. Profile"
        verbose_name_plural = "1. Profiles"


class VirtualCard(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='virtual_card', null=True)
    card_number = models.CharField("Card Number", max_length=20)
    mm_yy = models.CharField("MM/YY", max_length=50)
    cvc = models.CharField("CVC", max_length=3)
    zip_code = models.CharField("Zip Code", max_length=50)

    class Meta:
        verbose_name = "2. Virtual Card"
        verbose_name_plural = "2. Virtual Cards"

    def __str__(self):
        return self.card_number


class Portal(models.Model):
    name = models.CharField("Portal Name", max_length=255)
    code = models.CharField("Unique portal code", max_length=50, null=True, unique=True)

    class Meta:
        verbose_name = "3. Portal"
        verbose_name_plural = "3. Portals"

    def __str__(self):
        return self.name


class PortalGoal(models.Model):
    name = models.CharField("Custom portal name", max_length=50, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=200, blank=True, null=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='portal_goals')
    portals = models.ManyToManyField("Portal")

    class Meta:
        verbose_name = "4. Portal Goal"
        verbose_name_plural = "4. Portal Goals"

    def __str__(self):
        return "{}-portals-goals".format(self.profile)

    def get_absolute_url(self):
        if not self.slug:
            self.save()
        return reverse("user:portal_goals", kwargs={"slug": self.slug})


class UserData(models.Model):
    class Meta:
        verbose_name = "5. Personal Information"
        verbose_name_plural = "5. Personal Information"

    # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    duns = models.CharField("DUNS Number", null=True, blank=True, max_length=255)
    ein = models.CharField("EIN number", null=True, blank=True, max_length=255)

    first_name = models.CharField("First Name", null=True, blank=True, max_length=255)
    last_name = models.CharField("Last Name", null=True, blank=True, max_length=255)

    personal_street_address_1 = models.CharField("Personal Address Line 1", null=True, blank=True, max_length=255)
    personal_street_address_2 = models.CharField("Personal Address Line 2", null=True, blank=True, max_length=255)
    personal_zip_code = models.CharField("Personal Zip Code", null=True, blank=True, max_length=255)
    personal_city = models.CharField("Personal City", null=True, blank=True, max_length=255)
    personal_state = models.CharField("Personal State", null=True, blank=True, max_length=255)
    personal_country = models.CharField("Personal Country", null=True, blank=True, max_length=255)
    personal_phone = models.CharField("Personal Phone", null=True, blank=True, max_length=255)

    billing_street_address_1 = models.CharField("Billing Address Line 1", null=True, blank=True, max_length=255)
    billing_street_address_2 = models.CharField("Billing Address Line 2", null=True, blank=True, max_length=255)
    billing_zip_code = models.CharField("Billing Zip Code", null=True, blank=True, max_length=255)
    billing_city = models.CharField("Billing City", null=True, blank=True, max_length=255)
    billing_state = models.CharField("Billing State", null=True, blank=True, max_length=255)
    billing_country = models.CharField("Billing Country", null=True, blank=True, max_length=255)
    billing_phone = models.CharField("Billing Phone", null=True, blank=True, max_length=255)

    business_name = models.CharField("Business Name", null=True, blank=True, max_length=255)

    business_street_address_1 = models.CharField("Business Address Line 1", null=True, blank=True, max_length=255)
    business_street_address_2 = models.CharField("Business Address Line 2", null=True, blank=True, max_length=255)
    business_zip_code = models.CharField("Business Zip Code", null=True, blank=True, max_length=255)
    business_city = models.CharField("Business City", null=True, blank=True, max_length=255)
    business_state = models.CharField("Business State", null=True, blank=True, max_length=255)
    business_country = models.CharField("Business Country", null=True, blank=True, max_length=255)
    business_phone = models.CharField("Business Phone", null=True, blank=True, max_length=255)

    email = models.CharField("Email Address", null=True, blank=True, max_length=255)
    website = models.CharField("Website", null=True, blank=True, max_length=255)
    toll_free_number = models.CharField("Toll Free Number", null=True, blank=True, max_length=255)
    fax_number = models.CharField("Fax Number", null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if self.first_name == "":
            self.first_name = self.user.user.first_name
        if self.last_name == "":
            self.last_name = self.user.user.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name} personal details"


class UserSteps(models.Model):
    _choices = (
        (1, "Not ordered"),
        (2, "In progress"),
        (3, "Done"),
    )

    _industry_choices = (
        (1, "Electrician"),
        (2, "Gardener"),
        (3, "Tattoo Artist"),
        (4, "Photography"),
        (5, "Limo Service"),
        (6, "Nutrition Advisor"),
        (7, "Life Coach"),
        (8, "Veterinary clinic"),
        (9, "Laundromat"),
        (10, "Fitness Club"),
        (11, "Dentist"),
        (12, "Consulting"),
        (13, "Auto Repair"),
        (14, "Tutor"),
        (15, "Bakery"),
        (16, "Financial Advisor"),
        (17, "Lawyer"),
        (18, "Marketing Agency"),
        (19, "Trucking"),
        (20, "Locksmith"),
        (21, "Medical Clinic"),
        (22, "Dance Studio"),
        (23, "Carpenter"),
        (24, "Moving Company"),
        (25, "Hair Salon"),
        (26, "Cleaning Service"),
        (27, "Car Dealer"),
        (28, "Portfolio"),
        (29, "Real Estate"),
        (30, "Preschool"),
        (31, "Spa Service"),
        (32, "Physical Therapist"),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    email = models.CharField("User Email", max_length=500, null=False)
    first_name = models.CharField("First Name", max_length=500, null=True)
    last_name = models.CharField("Last Name", max_length=500, null=True)
    phone = models.CharField("Phone Number", max_length=500, null=True)

    website = models.IntegerField("Website", choices=_choices, null=True, default=1)
    industry_name = models.IntegerField("Industry", choices=_industry_choices, null=True, default=1, blank=True)

    toll_free_number = models.IntegerField("Toll free number", choices=_choices, null=True, default=1)
    fax_number = models.IntegerField("Fax numberx", choices=_choices, null=True, default=1)
    domain = models.IntegerField("Domain", choices=_choices, null=True, default=1)
    professional_email_address = models.IntegerField("Professional email", choices=_choices, null=True, default=1)
    business_builder_program = models.IntegerField("Business Builder Program", choices=_choices, null=True, default=1)

    base_professional_mailing_address = models.CharField("Base professional mailing address", null=True, default='', blank=True, max_length=500)

    domain_name = models.CharField("Domain name", null=True, default='', blank=True, max_length=500)

    fax_number_act = models.CharField("Actual fax number", null=True, default='', blank=True, max_length=500)
    toll_free_number_act = models.CharField("Actual toll free number", null=True, default='', blank=True,
                                            max_length=500)

    professional_email_address_act = models.CharField("Actual professional email address", null=True, default='',
                                                      blank=True, max_length=500)
    website_act = models.CharField("Actual website link", null=True, default='', blank=True, max_length=500)
    domain_act = models.CharField("Actual domain name", null=True, default='', blank=True, max_length=500)

    domain_dashboard = models.CharField("Domain name dashboard", null=True, default='', blank=True, max_length=500)
    email_provider = models.CharField("Email provider", null=True, default='', blank=True, max_length=500)

    toll_free_username = models.CharField("Toll Free Number username", null=True, default='', blank=True, max_length=500)
    toll_free_password = models.CharField("Toll Free Number password", null=True, default='', blank=True, max_length=500)
    toll_free_prefix = models.CharField("Toll Free prefix", null=True, default='', blank=True, max_length=500)
    toll_free_quantity = models.CharField("Toll Free amount", null=True, default='', blank=True, max_length=500)
    fax_number_prefix = models.CharField("Fax number prefix", null=True, default='', blank=True, max_length=500)
    fax_number_quantity = models.CharField("Fax amount amount", null=True, default='', blank=True, max_length=500)

    website_username = models.CharField("Website username", null=True, default='', blank=True, max_length=500)
    website_password = models.CharField("Website password", null=True, default='', blank=True, max_length=500)

    domain_username = models.CharField("Domain username", null=True, default='', blank=True, max_length=500)
    domain_password = models.CharField("Domain password", null=True, default='', blank=True, max_length=500)

    email_username = models.CharField("Email username", null=True, default='', blank=True, max_length=500)
    email_password = models.CharField("Email password", null=True, default='', blank=True, max_length=500)

    class Meta:
        verbose_name = "6. User Steps"
        verbose_name_plural = "6. User steps"

    def __str__(self):
        return f"{self.email} steps"
