from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import resolve

from kpi.models import SessionKPI, Url, SessionHistory


@receiver(pre_delete, sender=Session)
def session_deleted(sender, instance, **kwargs):
    session_kpi, created = SessionKPI.objects.get_or_create(key=instance.session_key)
    if not created:
        return

    data = instance.get_decoded()
    if '_auth_user_id' in data:
        user: User = User.objects.get(pk=data['_auth_user_id'])
        session_kpi.auth_username = user.username
    session_kpi.save()

    for history_dict in data['urls_history']:
        url_infos = resolve(history_dict['url_row'])
        url, _ = Url.objects.get_or_create(url_row=history_dict['url_row'], url_name=url_infos.url_name)

        history: SessionHistory = SessionHistory.objects.create(
            url=url,
            session=session_kpi,
            get_at=datetime.fromisoformat(history_dict['datetime']),
            track_source=history_dict['track'].get('track_source'),
        )

    session_kpi.calcul_kpis()
