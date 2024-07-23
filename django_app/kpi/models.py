from django.db import models as m


class Url(m.Model):
    full_url = m.CharField(max_length=200, primary_key=True)


class Session(m.Model):
    id = m.CharField(max_length=32, primary_key=True)
    is_authenticated = m.BooleanField(default=False)
