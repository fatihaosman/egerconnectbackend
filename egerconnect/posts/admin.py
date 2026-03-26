from django.contrib import admin
from .models import Events, Notice, LostAndFound, Scholarship, SupportRequest

admin.site.register(Notice)
admin.site.register(LostAndFound)
admin.site.register(Scholarship)
admin.site.register(Events)


@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    
    
#show useful columns in list view
    list_display = ("full_name", "type_of_need", "status", "created_at")
    
    # ✅ Filter by status
    list_filter = ("status",)
    
#keep fields readonly(admin-shouldnt be able to edit them manually)
    readonly_fields = [field.name for field in SupportRequest._meta.fields]
    
#prevent adding manually
    def has_add_permission(self, request):
        return False

# ACTIONS (bulk update status)
    actions = ["mark_as_accepted", "mark_as_declined"]

    def mark_as_accepted(self, request, queryset):
        queryset.update(status="accepted")
    mark_as_accepted.short_description = "Mark selected as Accepted"

    def mark_as_declined(self, request, queryset):
        queryset.update(status="declined")
    mark_as_declined.short_description = "Mark selected as Declined"