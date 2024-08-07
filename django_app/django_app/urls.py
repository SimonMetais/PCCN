from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, register_converter

from base import views
from django_app import settings
from django_app.converters import DatetimeConverter

register_converter(DatetimeConverter, 'dt')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test/', views.test, name='test'),

    path('', views.home, name='home'),
    path('adoption/', views.adoption, name='adoption'),
    path('protégés/', views.animals, name='animals'),
    path('protégés/<str:slug>/', views.animal, name='animal'),
    path('publications/', views.publications, name='publications'),
    path('publications/<dt:dt_publication>/', views.publication, name='publication'),
    path('partenaires/', views.sponsors, name='sponsors'),
]

if not settings.IN_PROD:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
