from pathlib import Path

from django.db import models as m
from django.urls import reverse
from django.utils.text import slugify


def image_path(instance, filename):
    return Path('animals', instance.slug + Path(filename).suffix)


class Animal(m.Model):
    name = m.CharField(max_length=50, unique=True, verbose_name="Nom")
    slug = m.SlugField(max_length=50, unique=True)
    breed = m.CharField(max_length=50, verbose_name="Race")
    birth = m.DateField(verbose_name="Date de naissance")
    arrival = m.DateField(verbose_name="Date d'arrivé")
    profile = m.ImageField(upload_to=image_path, verbose_name="Photo de profile")
    description = m.TextField()

    class Meta:
        ordering = ['-arrival']
        verbose_name = 'Protégé'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

    def get_absolute_url(self):
        return reverse('animal', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return str(self.name)
