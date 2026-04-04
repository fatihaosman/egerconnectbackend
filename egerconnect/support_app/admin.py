from django.contrib import admin
from .models import SupportMessage

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    # Remove "Add" button
    def has_add_permission(self, request):
        return False

    # Remove "Delete" button
    def has_delete_permission(self, request, obj=None):
        return False