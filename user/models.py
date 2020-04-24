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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15)
    fax_number_paid = models.BooleanField(default=False)
    toll_free_number_paid = models.BooleanField(default=False)
    website_creation_paid = models.BooleanField(default=False)
    objects = ProfileUserManager()

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)
