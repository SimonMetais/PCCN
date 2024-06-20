from django.db import models as m
from django.urls import reverse


class Home(m.Model):
    logo = m.ImageField(upload_to='Home/')
    home_text = m.TextField(verbose_name="Texte d'accueil")
    location = m.CharField(max_length=255, verbose_name="Adresse")

    class Meta:
        verbose_name = 'Accueil'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return "Modifier l'accueil"
