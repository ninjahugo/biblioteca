from django.conf.urls import patterns, include, url

# Descomenta las siguiente dos lineas
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    # INICIO
    url(r'^', include('apps.inicio.urls')),

    # AUTORES
    url(r'^autor/', include('apps.autores.urls')), 

)
