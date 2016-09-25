from django import forms
from django.utils.translation import ugettext as _


class PersonNameForm(forms.Form):
    first = forms.CharField(label=_('first name'), required=False)
    middle = forms.CharField(label=_('middle name'), required=False)
    last = forms.CharField(label=_('last name'))
    nickname = forms.CharField(label=_('nickname'), required=False)


class CompanyForm(forms.Form):
    name = forms.CharField(label=_('company name'))


class SpecialDateForm(forms.Form):
    occasion = forms.CharField(label=_('occasion'))
    date = forms.DateField(label=_('date'))


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
