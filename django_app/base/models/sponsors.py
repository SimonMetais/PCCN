from pathlib import Path

from django.db import models as m
from django.utils.text import slugify


def image_path(instance, filename):
    return Path('sponsors', instance.slug + Path(filename).suffix)


class Sponsor(m.Model):
    name = m.CharField(max_length=50, unique=True, verbose_name="Nom")
    slug = m.SlugField(max_length=50, unique=True)
    logo = m.ImageField(upload_to=image_path)
    website = m.CharField(max_length=255, unique=True, verbose_name="Site Web")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self) -> str:
        return str(self.name)
