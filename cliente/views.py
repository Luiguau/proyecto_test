from django.shortcuts import render, HttpResponse
from .models import Cliente

# Create your views here.

def inicio(request):
	# return HttpResponse("this is the equivalent of @app.route('/')!")
	return render(request, 'index.html')

def create(request):
	# reques.POST['parametro']
	Cliente.objects.create(
		nombre = request.POST['nombre'],
		apellido = request.POST['apellido'],
		rut = request.POST['rut'],
		dv = request.POST['dv'],
		direccion = request.POST['direccion'],
		email = request.POST['email'],
		password = request.POST['password'],
	)
	return render(request, 'index.html')

def read(request):
	#select * from cliente
	clients=Cliente.objects.all()
	return render(request, 'index.html')

def update(request):
	id= request.POST['id']
	client = Cliente.objects.get(id=id)
	# errors = Cliente.objects.validador_cliente(request.POST)
	errors = Cliente.objetos.validador_cliente(request.POST)


	if len(client) >0:
		client.nombre = request.POST['nombre']
		client.apellido = request.POST['apellido']
		client.rut = request.POST['rut']
		client.dv = request.POST['dv']
		client.direccion = request.POST['direccion']
		client.email = request.POST['email']
		client.password = request.POST['password']
	
	return render(request, 'index.html')

def delete(request):
	return render(request, 'index.html')
