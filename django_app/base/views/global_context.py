from base.models import Home


def global_data(request):
    home_stuffs: Home = Home.objects.first()
    return {
        'location': home_stuffs.location,
    }
