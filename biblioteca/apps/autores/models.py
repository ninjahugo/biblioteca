from django.db import models  

class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	foto = models.ImageField(upload_to='foto_autor')

	# colocando esta funcion en el admin sale el nombre de cada Autor
	def __unicode__(self):
		return self.nombre
