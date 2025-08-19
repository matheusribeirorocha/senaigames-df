# urls exclusivas do aplicativo crud_base
from django.urls import path
from . import views
urlpatterns=[
   path('',views.index,name='painel'),
   path('membro/',views.autentica_membro,name='membro')
]
