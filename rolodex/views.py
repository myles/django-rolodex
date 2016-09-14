# -*- coding: utf-8 -*-

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
    Contact,
)


class ContactCreateView(CreateView):

    model = Contact


class ContactDeleteView(CreateView):

    model = Contact


class ContactDetailView(DetailView):

    model = Contact


class ContactUpdateView(UpdateView):

    model = Contact


class ContactListView(ListView):

    model = Contact
