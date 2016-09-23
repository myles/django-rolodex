from django import forms
from django.utils.translation import ugettext as _


class PersonForm(forms.Form):
    first_name = forms.CharField(label=_('first name'))
    last_name = forms.CharField(label=_('last name'))
    


class EmailAddressForm(forms.Form):
    EMAIL_ADDRESS_CHOICES = (
        ('Work', 'Work'),
        ('Home', 'Home'),
        ('Other', 'Other')
    )

    location = forms.ChoiceField(label=_('location'),
                                 choices=EMAIL_ADDRESS_CHOICES)
    email_address = forms.EmailField(label=_('email address'))


class PhoneNumberForm(forms.Form):
    PHONE_NUMBER_CHOICES = (
        ('Mobile', 'Mobile'),
        ('Work', 'Work'),
        ('Home', 'Home'),
        ('Fax', 'Fax'),
        ('Pager', 'Pager'),
        ('Other', 'Other')
    )

    location = forms.ChoiceField(label=_('location'),
                                 choices=PHONE_NUMBER_CHOICES)
    phone_number = forms.CharField(label=_('phone number'))
