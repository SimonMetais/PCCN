from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views
from django_app import settings


urlpatterns = [
    path('', views.home, name='home'),

    path('protégés/', views.animals, name='animals'),
    path('protégés/<str:slug>/', views.animal, name='animal'),

    path('publications/', views.publications, name='publications'),
    path('publications/<int:pk>/', views.publication, name='publication'),

    path('partenaires/', views.sponsors, name='sponsors'),


    path('admin/', admin.site.urls),
]

if not settings.IN_PROD:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
