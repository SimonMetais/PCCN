from django.http import HttpRequest, HttpResponse
from django.utils.timezone import now

from django_app.settings import STATIC_URL, MEDIA_URL

black_list = {
    '/' + STATIC_URL,
    '/' + MEDIA_URL,
    '/favicon',
}


def kpi_middleware(get_response):
    def middleware(request: HttpRequest) -> HttpResponse:

        url_getted: str = request.path
        if any(url_getted.startswith(black) for black in black_list):
            return get_response(request)

        session = request.session
        if not session.get('init'):
            session['init'] = True
            session['urls_history'] = []

        session['urls_history'].append((url_getted, str(now())))
        return get_response(request)
    return middleware
