import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import urlize, linebreaks
from django.utils.safestring import mark_safe

register = template.Library()
url_pattern = re.compile(r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')


@register.filter
@stringfilter
def publication_format(texte: str, max_lenght):
    texte = linebreaks(texte)

    words = texte.split()
    if len(words) > max_lenght:
        texte = ' '.join(words[:max_lenght]) + '... <u>Voir la suite</u>'

    texte = url_pattern.sub(lambda x: urlize(x.group()), texte)
    return mark_safe(texte)
