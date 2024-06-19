from django.shortcuts import render

from base.models import Sponsor


def sponsors(request):
    all_sponsors = Sponsor.objects.all()
    return render(request, 'sponsors.html', context={'sponsors': all_sponsors})
