from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication


def home(request):
    home_stuffs: Home = Home.objects.first()
    quick_link_cards = {
        'donate': "<strong>Donnez</strong> pour eux",
        'adopt': "<strong>Adoptez</strong> un protégé",
        'volunteer': "Devenez <strong>volontaire</strong>",
    }
    context = {
        'last_publication': Publication.objects.first(),
        'q_cards': quick_link_cards.items(),
    }
    return render(request, 'home2.html', context=context)
