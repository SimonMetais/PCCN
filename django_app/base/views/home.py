from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication


def home(request):
    home_stuffs: Home = Home.objects.first()
    context = {
        'home_text': home_stuffs.home_text,
        'last_publication': Publication.objects.last(),
    }
    return render(request, 'home.html', context=context)
