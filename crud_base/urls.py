# urls exclusivas do app crud_base
from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_usuario, name='usuario')
    



]

