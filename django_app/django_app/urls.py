from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views
from django_app import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('partenaires/', views.sponsors, name='sponsors'),
    path('admin/', admin.site.urls),
]

if not settings.IN_PROD:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
