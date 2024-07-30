from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum, Count
from rangefilter.filters import DateRangeQuickSelectListFilterBuilder

from .models import SessionKPI, Url, SessionHistory

from django.contrib import admin


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_row', 'url_name', 'session_count')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SessionHistoryInline(admin.TabularInline):
    model = SessionHistory
    extra = 0
    readonly_fields = ('url', 'get_at')
    ordering = ('get_at',)


@admin.register(SessionKPI)
class SessionAdmin(ModelAdminTotals):
    list_display = (
        'pk', 'create_at', 'auth_username',
        'unique_urls_count', 'urls_count', 'is_rebond', 'session_time', 'first_track_source')
    inlines = [SessionHistoryInline]
    list_filter = (('create_at', DateRangeQuickSelectListFilterBuilder()), 'auth_username')
    list_totals = [('unique_urls_count', Sum), ('urls_count', Sum)]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
