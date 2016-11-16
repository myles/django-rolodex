from django import forms
from django.forms import formset_factory
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class PersonNameForm(forms.Form):
    first = forms.CharField(label=_('first name'), required=False)
    middle = forms.CharField(label=_('middle name'), required=False)
    last = forms.CharField(label=_('last name'))
    nickname = forms.CharField(label=_('nickname'), required=False)

    def __init__(self, *args, **kwargs):
        super(PersonNameForm, self).__init__(*args, **kwargs)

        self.auto_id = 'id_name_%s'

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset('name', 'first', 'middle', 'last', 'nickname'))


class CompanyNameForm(forms.Form):
    name = forms.CharField(label=_('company name'))

    def __init__(self, *args, **kwargs):
        super(CompanyNameForm, self).__init__(*args, **kwargs)

        self.auto_id = 'id_name_%s'

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout('name')


class SpecialDateForm(forms.Form):
    occasion = forms.CharField(label=_('occasion'))
    date = forms.DateField(label=_('date'))

    def __init__(self, *args, **kwargs):
        super(SpecialDateForm, self).__init__(*args, **kwargs)

        self.auto_id = 'id_name_%s'

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset('special date', 'occasion', 'date'))


class EmailAddressForm(forms.Form):
    EMAIL_ADDRESS_CHOICES = (
        ('Work', 'Work'),
        ('Home', 'Home'),
        ('Other', 'Other')
    )

    email_address = forms.EmailField(label=_('email address'))
    location = forms.ChoiceField(label=_('location'),
                                 choices=EMAIL_ADDRESS_CHOICES)

    def __init__(self, *args, **kwargs):
        super(EmailAddressForm, self).__init__(*args, **kwargs)

        self.auto_id = 'id_name_%s'

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset('email address', 'email_address', 'location'))


class PhoneNumberForm(forms.Form):
    PHONE_NUMBER_CHOICES = (
        ('Mobile', 'Mobile'),
        ('Work', 'Work'),
        ('Home', 'Home'),
        ('Fax', 'Fax'),
        ('Pager', 'Pager'),
        ('Other', 'Other')
    )

    phone_number = forms.CharField(label=_('phone number'))
    location = forms.ChoiceField(label=_('location'),
                                 choices=PHONE_NUMBER_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PhoneNumberForm, self).__init__(*args, **kwargs)

        self.auto_id = 'id_name_%s'

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset('phone number', 'phone_number', 'location'))


SpecialDateFormSet = formset_factory(SpecialDateForm)
EmailAddressFormSet = formset_factory(EmailAddressForm)
PhoneNumberFormSet = formset_factory(PhoneNumberForm)
