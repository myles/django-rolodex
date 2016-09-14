# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(regex='',
        view=TemplateView.as_view(template_name="base.html")),

    url(regex="^contact/~create/$",
        view=views.ContactCreateView.as_view(),
        name='contact_create'),

    url(regex="^contact/(?P<pk>\d+)/~delete/$",
        view=views.ContactDeleteView.as_view(),
        name='contact_delete'),

    url(regex="^contact/(?P<pk>\d+)/$",
        view=views.ContactDetailView.as_view(),
        name='contact_detail'),

    url(regex="^contact/(?P<pk>\d+)/~update/$",
        view=views.ContactUpdateView.as_view(),
        name='contact_update'),

    url(regex="^contact/$",
        view=views.ContactListView.as_view(),
        name='contact_list')
]
