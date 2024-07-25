from datetime import timedelta
from django.db import models as m


class ClosedSessionManager(m.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(create_at=None)


class SessionKPI(m.Model):
    key = m.CharField(max_length=32, primary_key=True, verbose_name="identifiant de session")
    auth_username = m.CharField(max_length=255, default=None, null=True, verbose_name="Nom d'utilisateur")
    urls = m.ManyToManyField('Url', through='SessionHistory')

    create_at = m.DateTimeField(editable=False, default=None, null=True, verbose_name="Vue sur le site le")
    urls_count = m.IntegerField(default=0, verbose_name="Nombre de pages visitées")
    unique_urls_count = m.IntegerField(default=0, verbose_name="Nombre de pages uniques visitées")
    is_rebond = m.BooleanField(default=False, verbose_name="Est un rebond")
    session_time = m.DurationField(default=None, null=True, verbose_name="Durée de la session")

    objects = m.Manager()
    all_closed = ClosedSessionManager()

    def calcul_kpis(self):
        self.create_at = self.history.first().get_at
        self.urls_count = self.urls.count()
        self.unique_urls_count = self.urls.distinct().count()
        self.is_rebond = self.urls_count == 1
        self.session_time = ((self.history.last().get_at - self.history.first().get_at) -
                             timedelta(microseconds=self.session_time.microseconds))
        self.save()

    class Meta:
        ordering = ['-create_at']
