from django.contrib import admin
from .models import Events, Notice, LostAndFound, Scholarship

admin.site.register(Notice)
admin.site.register(LostAndFound)
admin.site.register(Scholarship)
admin.site.register(Events)