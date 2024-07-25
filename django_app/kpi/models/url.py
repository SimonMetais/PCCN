from django.db import models as m


class Url(m.Model):
    url_row = m.CharField(max_length=255, unique=True)
    url_name = m.CharField(max_length=50, null=True, default=None)
    sessions = m.ManyToManyField('SessionKPI', through='SessionHistory')

    def session_count(self) -> int:
        return self.sessions.distinct().count()
    session_count.short_description = "Nombre de sesion à avoir visité cette url"

    def __str__(self):
        return self.url_name
