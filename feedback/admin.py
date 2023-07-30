from django.contrib import admin
from .models import Feedback, Address


@admin.register(Feedback)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact management section for admin
    """
    list_display = ['name']


admin.site.register(Address)