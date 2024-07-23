from django.contrib import admin
from .models import Session, Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('full_url', )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_authenticated', 'auth_username', 'urls_count', 'create_at')
