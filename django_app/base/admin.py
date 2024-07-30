
from django.contrib import admin
from django.contrib.auth.models import Group

from base.models import *


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    fields = ('name', 'detail', 'logo', 'website')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'arrival')
    fields = ('name', 'breed', 'birth', 'arrival', 'profile', 'description')


class PublicationAttachmentAdmin(admin.TabularInline):
    fields = ('file', 'file_type', 'image_preview')
    readonly_fields = ('file_type', 'image_preview')
    model = PublicationAttachment
    extra = 1


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    fields = ('description', )
    list_display = ('short_description', )
    inlines = (PublicationAttachmentAdmin, )


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)
