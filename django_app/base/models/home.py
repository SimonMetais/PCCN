from django.db import models as m


horaires = """
✅ Lun 10h-19h
✅ Mar 10h-19h
✅ Mer 10h-19h
✅ Jeu 10h-19h
✅ Ven 10h-19h
❌ Sam férmé
❌ Dim férmé
"""


class Home(m.Model):
    logo = m.ImageField(upload_to='Home/')
    home_text = m.TextField(verbose_name="Texte d'accueil", default="Bienvenue !")
    location = m.CharField(max_length=255, verbose_name="Adresse", default="6 rue des fleurs 17589 Queleque_part")
    phone_number = m.CharField(max_length=20, verbose_name="Numéro de téléphone", default="+33 (0)6 11 22 33 44")
    email = m.EmailField(verbose_name="e-mail", default="contact@exemple.com")
    opening_hours = m.TextField(verbose_name="Horaire d'ouverture", default=horaires)

    class Meta:
        verbose_name = 'Accueil'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return "Modifier l'accueil"
