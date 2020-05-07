from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse


class ProfileUserManager(models.Manager):
    def create_user(self, email, password, first_name, last_name, phone_number):
        user = User.objects.create_user(email=email, username=email, password=password, first_name=first_name,
                                        last_name=last_name)
        profile = Profile(user=user, phone_number=phone_number)
        profile.save()
        return profile


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15)
    fax_number_paid = models.BooleanField(default=False)
    toll_free_number_paid = models.BooleanField(default=False)
    website_creation_paid = models.BooleanField(default=False)
    virtual_access_card_paid = models.BooleanField(default=False)
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
