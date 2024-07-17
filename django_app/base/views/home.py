from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication


def home(request):
    home_stuffs: Home = Home.objects.first()
    quick_link_cards = {
        'donate': ("<strong>Donnez</strong> pour eux", 'https://www.helloasso.com/associations/pccn#highlight'),
        'adopt': ("<strong>Adoptez</strong> un protégé", '#'),
        'volunteer': ("Devenez <strong>volontaire</strong>", 'https://www.helloasso.com/associations/pccn/adhesions/adhesion-1'),
    }
    context = {
        'last_publication': Publication.objects.first(),
        'q_cards': quick_link_cards.items(),
    }
    return render(request, 'home.html', context=context)
