from django.db import models
import re

# aca se definen los campos que tendra mi tabla en la base de datos (vamos a modelar la base de datos)

# Create your models here.
# class Client_Manager(models.Manager):
# 	#esta clase sirve para crear todos metodos que permitiran
# 	#las validaciones de los datos

# 	def clientValidator(self, data):
# 		#errors guardara todos los errores que se encuentren durante las validaciones
# 		errors={} #diccionario de errores
# 		if len(data['nombre']) == 0:
# 			errors['nombre']='Ingrese un nombre'
# 		if len(data['apellido']) == 0:
# 			errors['apellido']='Ingrese un apellido'
# 		if len(data['rut']) == 0:
# 			errors['rut']='Ingrese un rut'
# 		if len(data['dv']) == 0:
# 			errors['dv']='Ingrese un dv'
# 		if len(data['direccion']) == 0:
# 			errors['direccion']='Ingrese una direccion'
# 		#esto es una expresion regular para validar los datos ingresados
# 		EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# 		if not EMAIL.match(data['email']):
# 			errors['email'] = "email invalido"
# 		return errors

class ClienteManager(models.Manager):
	def validador_cliente(self, data):
		errores = {}
		if len(data['nombre']) == 0:
			errores['nombre'] = 'Ingrese un nombre'
		if len(data['apellido']) == 0:
			errores['apellido'] = 'Ingrese un apellido'
		if len(data['rut']) == 0:
			errores['rut'] = 'Ingrese un rut'
		if len(data['dv']) == 0:
			errores['dv'] = 'Ingrese un dv'
		# expresiones regulares para validar los datos ingresados
		EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not EMAIL.match(data['email']):
			errores['email'] = "email invalido"
		if len(data['direccion']) == 0:
			errores['direccion'] = 'Ingrese una direccion'
		return errores


class Cliente(models.Model):
	# cada atributo es una columna que tendra la tabla
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	rut = models.CharField(max_length=12)
	dv = models.CharField(max_length=1)
	direccion = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=10)
	# los siguientes atributos se crean siempre para temas de reporteria
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# se creara una clase manager
	objects = ClienteManager()
	objetos = ClienteManager()

	# objects = Client_Manager()
	# objetos = Client_Manager()
