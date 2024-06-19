
from django.contrib import admin

from base.models import Sponsor, Animal, Publication, PublicationAttachment


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    fields = ('name', 'logo')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
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
