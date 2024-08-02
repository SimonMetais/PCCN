from django.core.validators import FileExtensionValidator
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
    logo = m.FileField(verbose_name="Logo (en .SVG uniquement)", upload_to='Home/', validators=[FileExtensionValidator(['svg'])])
    home_text = m.TextField(verbose_name="Texte d'accueil", default="Bienvenue !")
    home_picture = m.FileField(verbose_name="Image d'accueil", upload_to='Home/', null=True, blank=True)
    location = m.CharField(max_length=255, verbose_name="Adresse", default="6 rue des fleurs 17589 Queleque_part")
    phone_number = m.CharField(max_length=20, verbose_name="Numéro de téléphone", default="+33 (0)6 11 22 33 44")
    email = m.EmailField(verbose_name="e-mail", default="contact@exemple.com")
    opening_hours = m.TextField(verbose_name="Horaire d'ouverture", default=horaires)
    adoption_text = m.TextField(verbose_name="texte d'adoption", blank=True)

    class Meta:
        verbose_name = 'Accueil'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return "Modifier l'accueil"
