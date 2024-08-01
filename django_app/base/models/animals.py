from pathlib import Path

from django.db import models as m
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now


def image_path(instance, filename):
    return Path('animals', instance.slug + Path(filename).suffix)


class Animal(m.Model):
    name = m.CharField(max_length=50, unique=True, verbose_name="Nom")
    slug = m.SlugField(max_length=50, unique=True)
    breed = m.CharField(max_length=50, verbose_name="Race")
    birth = m.DateField(verbose_name="Date de naissance")
    arrival = m.DateField(verbose_name="Date d'arrivé")
    departure = m.DateField(verbose_name="Date de départ", null=True, default=None, blank=True)
    profile = m.ImageField(upload_to=image_path, verbose_name="Photo de profile")
    description = m.TextField(max_length=460)
    sexe = m.CharField(max_length=1, choices=[
        ('F', 'Femelle'),
        ('M', 'Mâle'),
    ])

    class Meta:
        ordering = ['-arrival']
        verbose_name = 'Protégé'

    @property
    def age(self):
        today = now().date()
        age = int(
            today.year
            - self.birth.year
            - ((today.month, today.day) < (self.birth.month, self.birth.day))
        )
        return age

    @property
    def e(self):
        return 'e' if self.sexe == 'F' else ''

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

    def get_absolute_url(self):
        return reverse('animal', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return str(self.name)
