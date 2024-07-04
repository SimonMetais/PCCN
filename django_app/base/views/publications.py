from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from base.models import Publication


def publications(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Publication.objects.all(), 4)
    page_obj = paginator.get_page(page_number)
    return render(request, 'publications.html', context={'publications': page_obj})


def find_publication(dt_publication: datetime) -> Publication:
    return get_object_or_404(Publication,
                             post_at__year=dt_publication.year,
                             post_at__month=dt_publication.month,
                             post_at__day=dt_publication.day,
                             post_at__hour=dt_publication.hour,
                             post_at__minute=dt_publication.minute,
                             post_at__second=dt_publication.second)


def publication(request, dt_publication: datetime):
    the_publication = find_publication(dt_publication)
    return render(request, 'publication.html', context={'publication': the_publication})
