from django.shortcuts import render, get_object_or_404

from base.models import Animal


def animals(request):
    all_animals = Animal.objects.all()
    return render(request, 'animals/animals.html', context={'animals': all_animals})


def animal(request, slug):
    the_animal = get_object_or_404(Animal, slug=slug)
    return render(request, 'animals/animal.html', context={'animal': the_animal})
