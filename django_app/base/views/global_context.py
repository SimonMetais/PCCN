from base.models import Home


def global_data(request):
    header = {
        'Protégés': 'animals',
        'Publications': 'publications',
        'Partenaires': 'sponsors',
    }
    return {
        'header_list': header.items(),
        'home_stuffs': Home.objects.first(),
    }

