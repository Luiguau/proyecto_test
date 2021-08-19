from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    #CRUD
    path('create', views.create), #create
    path('read', views.read), #read
    path('update', views.update), #update
    path('delete', views.delete), #delete
	
]