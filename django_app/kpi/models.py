from datetime import datetime

from django.db import models as m


class Url(m.Model):
    full_url = m.CharField(max_length=200, primary_key=True)  # TODO a ne pas mettre en pk, long en base pour rien


class Session(m.Model):
    id = m.CharField(max_length=32, primary_key=True)
    is_authenticated = m.BooleanField(default=False)
    auth_username = m.CharField(max_length=255, default=None, null=True)
    create_at = m.DateTimeField(editable=False, auto_now_add=True, verbose_name="Vue sur le site le")
    urls = m.ManyToManyField(Url, through='SessionHistory')

    class Meta:
        ordering = ['-create_at']

    def urls_count(self) -> int:
        return self.urls.count()
    urls_count.short_description = "Nombre d'url visités"


class SessionHistory(m.Model):
    url = m.ForeignKey(Url, m.CASCADE, 'history')
    session = m.ForeignKey(Session, m.CASCADE, 'history')
    get_at = m.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ['get_at']
