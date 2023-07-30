from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactManage(admin.ModelAdmin):
    display_all = [
        "date_submitted",
        "name",
        "heading",
        "message_body",
        "acknowledged"
        ]
    list_filter = ["date_submitted", "name", "acknowledged"]
    search_fields = ["name", "heading", "message_body"]
    date_hierarchy = "date_submitted"