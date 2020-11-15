from django import forms

from dynamic.models import Subdomain


class WhiteLabelForm(forms.ModelForm):
    logo = forms.ImageField(required=False)
    class Meta:
        model = Subdomain
        exclude = [
            'is_payment_done',
            'sub_name',
            'admins',
            'show_becoming_whitelabel_partner',
            'offer_paid_whitelabel',
            'appImage',
            'iphoneApp',
            'androidApp',
            'chromeExt',
            'extensionVideo',
            'affiliate_link',
            'whitelabelpartner_link',
            'show_free_access_to_affiliate_program',
            'whitelabel_index_video',
            'is_main_site',
            'faq_page',
            'is_paid_for_whitelabel'
        ]



