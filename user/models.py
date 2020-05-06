from django.db import models
from django.contrib.auth.models import User


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
    portals = models.ManyToManyField("Portal", related_name='portals_subscribed', blank=True)
    objects = ProfileUserManager()

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)


class VirtualCard(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='virtual_card', null=True)
    card_number = models.CharField("Card Number", max_length=20)
    mm_yy = models.CharField("MM/YY", max_length=50)
    cvc = models.CharField("CVC", max_length=3)
    zip_code = models.CharField("Zip Code", max_length=50)

    class Meta:
        verbose_name = "Virtual Card"
        verbose_name_plural = "Virtual Cards"

    def __str__(self):
        return self.card_number


class Portal(models.Model):
    name = models.CharField("Portal Name", max_length=255)

    class Meta:
        verbose_name = "Portal"
        verbose_name_plural = "Portals"

    def __str__(self):
        return self.name
