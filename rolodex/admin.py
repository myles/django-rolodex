from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_type', 'modified', 'owner')
    list_filter = ('contact_type', 'owner')
    search_fields = ['data']


admin.site.register(Contact, ContactAdmin)