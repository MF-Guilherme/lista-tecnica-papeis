from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar_ciclo/', views.cadastrar_ciclo, name='cadastrar_ciclo'),
    path('cadastrar_versao/', views.cadastrar_versao, name='cadastrar_versao'),
]
