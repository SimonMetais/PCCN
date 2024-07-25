from datetime import datetime
from pprint import pprint

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

    for row_url, str_dt in data['urls_history']:
        url_infos = resolve(row_url)
        dt = datetime.fromisoformat(str_dt)

        url, _ = Url.objects.get_or_create(url_row=row_url, url_name=url_infos.url_name)
        history = SessionHistory.objects.create(url=url, session=session_kpi, get_at=dt)

    session_kpi.calcul_kpis()
