from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication


def home(request):
    home_stuffs: Home = Home.objects.first()
    context = {
        'last_publication': Publication.objects.first(),
    }
    return render(request, 'home2.html', context=context)
