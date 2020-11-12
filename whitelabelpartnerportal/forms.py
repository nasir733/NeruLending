from django import forms

from dynamic.models import Subdomain


class WhiteLabelForm(forms.ModelForm):
    logo = forms.ImageField(required=False)
    class Meta:
        model = Subdomain
        exclude = ['is_payment_done', 'sub_name', 'admins']



