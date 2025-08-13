# urls exclusivas do app crud_base
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.painel, name='painel')
    ]
