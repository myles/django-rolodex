# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import JSONField

from model_utils.models import TimeStampedModel

CONTACT_TYPE_CHOCIES = (
    ('person', 'Person'),
    ('company', 'Company')
)


class Contact(TimeStampedModel):
    """
    Contact model.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    contact_type = models.CharField(max_length=10,
                                    choices=CONTACT_TYPE_CHOCIES)
    data = JSONField()

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                              limit_choices_to={'is_active': True})

    class Meta:
        db_table = 'rolodex_contacts'
        ordering = ('modified', 'created',)
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return "{}".format(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('rolodex:contact_detail', None, {
            'pk': self.pk,
            'slug': self.slug
        })

    # @models.permalink
    # def get_update_url(self):
    #     return ('rolodex:contact_update', None, {
    #         'pk': self.pk,
    #         'slug': self.slug
    #     })

    # @models.permalink
    # def get_delete_url(self):
    #     return ('rolodex:contact_delete', None, {
    #         'pk': self.pk,
    #         'slug': self.slug
    #     })

    @property
    def slug(self):
        return slugify(self.name)

    def get_name(self):
        if self.contact_type == 'company':
            return "{name}".format(**self.data)
        elif self.contact_type == 'person':
            return "{name[first]} {name[last]}".format(**self.data)
        else:
            return "Unknown"

    def save(self, *args, **kwargs):
        self.name = self.get_name()
        super(Contact, self).save(*args, **kwargs)
