from django.contrib import admin
from .models import ClubImage, Events, Notice, LostAndFound, Scholarship, SupportRequest, Club

admin.site.register(Notice)
admin.site.register(LostAndFound)
admin.site.register(Scholarship)
admin.site.register(Events)

# ❌ REMOVE THIS
# admin.site.register(Club)

@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "type_of_need", "status", "created_at")
    list_filter = ("status",)
    readonly_fields = [field.name for field in SupportRequest._meta.fields]

    def has_add_permission(self, request):
        return False

    actions = ["mark_as_accepted", "mark_as_declined"]

    def mark_as_accepted(self, request, queryset):
        queryset.update(status="accepted")

    def mark_as_declined(self, request, queryset):
        queryset.update(status="declined")


class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 3

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubImageInline]