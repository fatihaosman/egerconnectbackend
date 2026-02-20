from django.contrib import admin
from .models import Events, Notice, LostAndFound, Scholarship, SupportRequest

admin.site.register(Notice)
admin.site.register(LostAndFound)
admin.site.register(Scholarship)
admin.site.register(Events)


@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in SupportRequest._meta.fields]

    def has_add_permission(self, request):
        return False