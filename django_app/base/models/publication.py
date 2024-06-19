import mimetypes
from pathlib import Path

from django.db import models as m
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html


class Publication(m.Model):
    description = m.TextField()
    post_at = m.DateTimeField(editable=False, auto_now_add=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def get_absolute_url(self):
        return reverse('publication', kwargs={'pk': self.pk})


class PublicationAttachment(m.Model):
    file = m.FileField('Média', upload_to='publications/')
    file_type = m.CharField('Type de média', max_length=1, editable=False)
    publication = m.ForeignKey(Publication, m.CASCADE, 'Attachments')

    class Meta:
        verbose_name = 'Média'
        verbose_name_plural = 'Médias'

    def determine_file_type(self):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        video_extensions = ['.mp4', '.avi', '.mov']
        extension = Path(self.file.name).suffix.lower()
        match extension:
            case ext if ext in image_extensions:
                return extension, 'Image'
            case ext if ext in video_extensions:
                return extension, 'Video'
            case _:
                return extension, 'Inconnue'

    def save(self, *args, **kwargs):
        _, self.file_type = self.determine_file_type()
        super().save(*args, **kwargs)

    def image_preview(self):
        extension, file_type = self.determine_file_type()
        if file_type == 'Image':
            return format_html(f'<img src="{self.file.url}" style="max-width: 200px; max-height: 200px;" />')
        elif file_type == 'Video':
            mime_type, _ = mimetypes.guess_type(self.file.url)
            return format_html(f'<video width="200" controls><source src="{self.file.url}" type="{mime_type}">Your browser does not support the video tag.</video>')
        else:
            return format_html('No preview available')
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
