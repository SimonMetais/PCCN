from django.shortcuts import render, get_object_or_404

from base.models import Home


def home(request):
    context = {
        'home_stuffs': Home.objects.first(),
    }
    return render(request, 'home.html', context=context)
