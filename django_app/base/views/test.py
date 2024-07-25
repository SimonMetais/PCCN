from datetime import timedelta
from pprint import pprint

from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.timezone import now


def test(request):
    session_key = request.session.session_key
    request.session.save()

    pprint(request.session.get('urls_history'))

    session = Session.objects.get(session_key=session_key)
    logout(request)
    session.delete()
    return HttpResponseRedirect(reverse('home'))
