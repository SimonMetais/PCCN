from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication


def test(request):
    home_stuffs: Home = Home.objects.first()
    context = {
        'home_text': home_stuffs.home_text if home_stuffs else None,
        'last_publication': Publication.objects.last(),
    }
    return render(request, 'test.html', context=context)
