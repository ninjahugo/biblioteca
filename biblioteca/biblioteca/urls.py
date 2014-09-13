from django.conf.urls import patterns, include, url 
from django.conf import settings

# Descomenta las siguiente dos lineas
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root':settings.MEDIA_ROOT, }),

    # INICIO
    url(r'^', include('apps.inicio.urls')),

    # AUTORES
    url(r'^autor/', include('apps.autores.urls')), 

)
