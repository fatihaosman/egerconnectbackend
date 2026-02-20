from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "registration_number")
    readonly_fields = [field.name for field in User._meta.fields]

    def has_add_permission(self, request):
        return False
