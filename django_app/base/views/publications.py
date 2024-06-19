from django.shortcuts import render, get_object_or_404

from base.models import Publication


def publications(request):
    all_publications = Publication.objects.all()
    return render(request, 'publications.html', context={'publications': all_publications})


def publication(request, pk):
    the_publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publication.html', context={'publication': the_publication})
