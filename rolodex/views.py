# -*- coding: utf-8 -*-

from django.views import View
from django.shortcuts import redirect
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render

from .models import Contact
from .forms import (PersonNameForm, CompanyNameForm, SpecialDateFormSet,
                    EmailAddressFormSet, PhoneNumberFormSet)


class ContactListView(View):
    """Get a list of contacts in the database."""

    template_name = 'rolodex/contact_list.html'

    def get(self, request, *args, **kwargs):
        contact_list = Contact.objects.all()

        return render(request, self.template_name,
                      {'object_list': contact_list})


class ContactDetailView(View):
    """Get an individual contact in the database."""

    template_name = 'rolodex/contact_detail.html'

    def get(self, request, pk, slug=None, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=pk)

        # Make sure we redirect if the slug in the view doesn't match the slug
        # in the database.
        if not slug or contact.slug != slug:
            return redirect(contact.get_absolute_url())

        return render(request, self.template_name, {'object': contact})


class ContactCreateView(View):
    """Create a contact in the database."""

    # Helper fuctions
    def get_forms(self, contact_type, request_post=None):
        # Load up the forms
        forms = {
            'special_date': SpecialDateFormSet(request_post,
                                               prefix='special_date'),
            'email_address': EmailAddressFormSet(request_post,
                                                 prefix='email_address'),
            'phone_number': PhoneNumberFormSet(request_post,
                                               prefix='phone_number')
        }

        # Add the correct vertical forms for the contact type.
        if contact_type == 'person':
            forms['name'] = PersonNameForm(request_post, prefix='name')
        elif contact_type == 'company':
            forms['name'] = CompanyNameForm(request_post, prefix='name')

        return forms

    # HTTP request methods
    def get(self, request, contact_type, *args, **kwargs):
        # We only support two types of contacts, people and companies.
        if contact_type not in ['person', 'company']:
            raise Http404

        context = {
            'forms': self.get_forms(contact_type),
            'contact_type': contact_type
        }

        return render(request, 'rolodex/contact_create.html', context)

    def post(self, request, contact_type, *args, **kwargs):
        # We only support two types of contacts, people and companies.
        if contact_type not in ['person', 'company']:
            raise Http404

        forms = self.get_forms(contact_type, request.POST)

        if not all(form.is_valid() for form in forms.values()):
            raise HttpResponseBadRequest

        # FIXME This works but looks ugly.
        form_name = forms['name']
        del(forms['name'])

        data = {}

        if contact_type == 'company':
            data['name'] = form_name.cleaned_data['name']
        elif contact_type == 'person':
            data['name'] = form_name.cleaned_data

        contact = Contact.objects.create(data=data, contact_type=contact_type,
                                         owner=request.user)

        return redirect(contact.get_absolute_url())
