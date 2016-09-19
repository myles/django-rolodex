# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(regex=r'^$',
        view=TemplateView.as_view(template_name="base.html")),

    url(regex=r"^contact/~create/$",
        view=views.ContactCreateView.as_view(),
        name='contact_create'),

    url(regex=r"^contact/(?P<pk>\d+)-(?P<slug>[-\w]+)/~delete/$",
        view=views.ContactDeleteView.as_view(),
        name='contact_delete'),

    url(regex=r"^contact/(?P<pk>\d+)/$",
        view=views.ContactDetailRedirectView.as_view(),
        name='contact_detail_without_slug'),

    url(regex=r"^contact/(?P<pk>\d+)-(?P<slug>[-\w]+)/$",
        view=views.ContactDetailView.as_view(),
        name='contact_detail'),

    url(regex=r"^contact/(?P<pk>\d+)-(?P<slug>[-\w]+)/~update/$",
        view=views.ContactUpdateView.as_view(),
        name='contact_update'),

    url(regex=r"^contact/$",
        view=views.ContactListView.as_view(),
        name='contact_list')
]
