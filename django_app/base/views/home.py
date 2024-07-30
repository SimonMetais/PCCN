from django.shortcuts import render, get_object_or_404

from base.models import Home, Publication, Animal


def home(request):
    home_stuffs: Home = Home.objects.first()
    quick_link_cards = {
        'donate': ("<strong>Donnez</strong> pour eux", 'https://www.helloasso.com/associations/pccn#highlight'),
        'adopt': ("Devenez <strong>famille d'accueil</strong>", '#'),
        'volunteer': ("Devenez <strong>volontaire</strong>", 'https://www.helloasso.com/associations/pccn/adhesions/adhesion-1'),
    }
    context = {
        # 'last_publication': Publication.objects.first(),
        'last_animals': Animal.objects.all()[:3],
        'q_cards': quick_link_cards.items(),
    }
    return render(request, 'home.html', context=context)
