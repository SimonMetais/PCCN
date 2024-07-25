from django.db import models as m


class SessionHistory(m.Model):
    url = m.ForeignKey('Url', m.CASCADE, 'history')
    session = m.ForeignKey('SessionKPI', m.CASCADE, 'history')
    get_at = m.DateTimeField(editable=False, verbose_name="Requétée le")

    class Meta:
        ordering = ['get_at']
        verbose_name = 'Historique de la session'
        verbose_name_plural = verbose_name
