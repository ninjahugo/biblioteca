#-*- coding: utf-8 -*- 
from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.views.generic import TemplateView
import urllib

class index(TemplateView):
	
	def get(self, request, *args, **kwargs):
		return render_to_response('inicio/index.html',
			context_instance = RequestContext(request))

class index2(TemplateView):
	template_name = 'inicio/index2.html'


def my_image5(request):
	linea = []
	for i in range(1,20):
		try:
#			imagen = urllib.quote('http://www.covercaratulas.com/ode/mini/carteles-%d.jpg'%i)
			imagen = urllib.quote('http://baulabuela.files.wordpress.com/2014/09/alexandre-rampazo-%d.jpg'%i)
			linea = linea +[imagen]
			
		except IOError:
			print "No encontre el archivo"

	dato =[]
	print dato
	for x in linea:
		lineas = str(x)
		if len(lineas) >= 64 :
		    dato = dato +[lineas[-64:]]
		elif len(lineas) >64:
			dato = dato +[lineas[-65:]]


	contexto = {'datos':dato}
	return render_to_response('inicio/my_image5.html',contexto,context_instance=RequestContext(request))

