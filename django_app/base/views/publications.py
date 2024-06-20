from datetime import datetime

from django.shortcuts import render, get_object_or_404

from base.models import Publication


def publications(request):
    all_publications = Publication.objects.all()
    return render(request, 'publications.html', context={'publications': all_publications})


def publication(request, dt: datetime):
    the_publication = get_object_or_404(Publication,
                                        post_at__year=dt.year,
                                        post_at__month=dt.month,
                                        post_at__day=dt.day,
                                        post_at__hour=dt.hour,
                                        post_at__minute=dt.minute,
                                        post_at__second=dt.second)
    return render(request, 'publication.html', context={'publication': the_publication})
