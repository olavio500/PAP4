
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('cadastro', views.cadast, name='cadastro'),
    path('login', views.logar, name='login' ),
    path('index', views.principal, name='index'),
    path('lognout', views.lognout, name='lognout.html')

]
