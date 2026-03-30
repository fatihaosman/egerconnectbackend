# reports/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

class ReportAdmin(admin.ModelAdmin):
    change_list_template = "reports/dashboard.html"  # use our template

