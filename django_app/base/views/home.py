from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication


def home(request):
    home_stuffs: Home = Home.objects.first()
    quick_link_cards = {
        'donate': ("<strong>Donnez</strong> pour eux", 'https://www.google.com/'),
        'adopt': ("<strong>Adoptez</strong> un protégé", 'https://www.google.com/'),
        'volunteer': ("Devenez <strong>volontaire</strong>", 'https://www.google.com/'),
    }
    context = {
        'last_publication': Publication.objects.first(),
        'q_cards': quick_link_cards.items(),
    }
    return render(request, 'home.html', context=context)
