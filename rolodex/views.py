# -*- coding: utf-8 -*-

from django.views import View
from django.shortcuts import get_object_or_404, redirect, render

from .models import Contact


class ContactListView(View):
    template_name = 'rolodex/contact_list.html'

    def get(self, request, *args, **kwargs):
        contact_list = Contact.objects.all()

        return render(request, self.template_name,
                      {'object_list': contact_list})


class ContactDetailView(View):
    template_name = 'rolodex/contact_detail.html'

    def get(self, request, pk, slug=None, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=pk)

        if not slug or contact.slug != slug:
            return redirect(contact.get_absolute_url())

        return render(request, self.template_name, {'object': contact})
