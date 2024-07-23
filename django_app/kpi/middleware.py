from django_app.settings import STATIC_URL, MEDIA_URL
from .models import Session, Url, SessionHistory

black_list = {
    '/' + STATIC_URL,
    '/' + MEDIA_URL,
    '/admin'
}


def kpi_middleware(get_response):
    def middleware(request):

        # --------------------  Création des instances  --------------------
        request.session['init'] = True
        session_id: str = request.session.session_key
        url_getted: str = request.path

        if session_id is None or any(url_getted.startswith(black) for black in black_list):
            return get_response(request)

        if request.user.is_authenticated:
            session, _ = Session.objects.get_or_create(id=session_id,
                                                       is_authenticated=True,
                                                       auth_username=request.user.username)
        else:
            session, _ = Session.objects.get_or_create(id=session_id)
        url, _ = Url.objects.get_or_create(full_url=url_getted)

        # --------------------  link  --------------------
        SessionHistory(url=url, session=session).save()

        return get_response(request)
    return middleware
