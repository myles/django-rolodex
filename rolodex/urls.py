# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(regex=r"^$",
        view=views.ContactListView.as_view(),
        name='contact_list'),

    url(regex=r"^(?P<pk>\d+)/$",
        view=views.ContactDetailView.as_view()),

    url(regex=r"^(?P<pk>\d+)-(?P<slug>[-\w]+)/$",
        view=views.ContactDetailView.as_view(),
        name='contact_detail'),

    # url(regex=r"^contact/~create/$",
    #     view=views.ContactCreateView.as_view(),
    #     name='contact_create'),

    # url(regex=r"^contact/(?P<pk>\d+)-(?P<slug>[-\w]+)/~delete/$",
    #     view=views.ContactDeleteView.as_view(),
    #     name='contact_delete'),

    # url(regex=r"^contact/(?P<pk>\d+)-(?P<slug>[-\w]+)/~update/$",
    #     view=views.ContactUpdateView.as_view(),
    #     name='contact_update'),
]
