import mimetypes
from pathlib import Path

from django.db import models as m
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html
from django.utils.timezone import now

from django_app.converters import datetime_url_format


def image_path(instance, filename):
    return Path('publications', instance.publication.post_at.strftime(datetime_url_format), Path(filename).name)


class Publication(m.Model):
    description = m.TextField()
    post_at = m.DateTimeField(editable=False, auto_now_add=True)
    is_last_of_month = m.BooleanField(default=True, editable=False)

    class Meta:
        ordering = ['-post_at']

    def save(self, *args, **kwargs):
        if not self.pk:
            n = now()
            try:
                second_to_last_of_month: Publication = Publication.objects.get(
                    post_at__year=n.year, post_at__month=n.month,
                    is_last_of_month=True)
            except Publication.DoesNotExist:
                pass
            else:
                second_to_last_of_month.is_last_of_month = False
                second_to_last_of_month.save()
        super(Publication, self).save(*args, **kwargs)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def get_absolute_url(self):
        return reverse('publication', kwargs={'dt_publication': self.post_at})


class PublicationAttachment(m.Model):
    file = m.FileField('Média', upload_to=image_path)
    file_type = m.CharField('Type de média', max_length=10, editable=False)
    publication = m.ForeignKey(Publication, m.CASCADE, 'attachments')

    class Meta:
        verbose_name = 'Média'

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
            return format_html(
                f'<video width="200" controls><source src="{self.file.url}" type="{mime_type}">Your browser does not support the video tag.</video>')
        else:
            return format_html('No preview available')

    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
