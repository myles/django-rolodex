# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import (RedirectView, CreateView, DeleteView,
                                  DetailView, UpdateView, ListView)

from .models import Contact


class ContactDetailRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'contact_detail'

    def get_redirect_url(self, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=kwargs['pk'])
        return contact.get_absolute_url()


class ContactCreateView(CreateView):

    model = Contact


class ContactDeleteView(DeleteView):

    model = Contact


class ContactDetailView(DetailView):

    model = Contact


class ContactUpdateView(UpdateView):

    model = Contact


class ContactListView(ListView):

    model = Contact
