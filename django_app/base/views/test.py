from pprint import pprint

from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.urls import reverse


def test(request):
    session_key = request.session.session_key
    pprint(request.session.get('urls_history'))
    session = Session.objects.get(session_key=session_key)
    logout(request)
    session.delete()
    return HttpResponseRedirect(reverse('home'))
