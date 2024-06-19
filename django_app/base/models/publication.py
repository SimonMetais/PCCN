from django.db import models as m


class Publication(m.Model):
    description = m.TextField()
    post_at = m.DateTimeField(editable=False, auto_now_add=True)


class Attachment(m.Model):
    class AttachmentType(m.TextChoices):
        PHOTO = 'P', "Photo"
        VIDEO = 'V', "Video"

    file = m.ImageField('Média', upload_to='publications/')
    file_type = m.CharField('Type de média', choices=AttachmentType, max_length=1, default=AttachmentType.PHOTO)
    publication = m.ForeignKey(Publication, m.CASCADE, 'Attachments')

    class Meta:
        verbose_name = 'Média'
        verbose_name_plural = 'Médias'
