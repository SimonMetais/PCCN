from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum, Count
from rangefilter.filters import DateRangeQuickSelectListFilterBuilder

from .models import SessionKPI, Url, SessionHistory


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_row', 'url_name', 'session_count')


class SessionHistoryInline(admin.TabularInline):
    model = SessionHistory
    extra = 0
    readonly_fields = ('url', 'get_at')
    ordering = ('get_at',)


@admin.register(SessionKPI)
class SessionAdmin(ModelAdminTotals):
    list_display = (
        'pk', 'create_at', 'auth_username',
        'unique_urls_count', 'urls_count', 'is_rebond', 'session_time')
    inlines = [SessionHistoryInline]
    list_filter = (('create_at', DateRangeQuickSelectListFilterBuilder()), 'auth_username')
    list_totals = [('unique_urls_count', Sum), ('urls_count', Sum)]
