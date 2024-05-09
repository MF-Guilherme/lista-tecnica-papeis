from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar_ciclo/', views.cadastrar_ciclo, name='cadastrar_ciclo'),
    path('cadastrar_versao/', views.cadastrar_versao, name='cadastrar_versao'),
    path('cadastrar_acabamento/', views.cadastrar_acabamento, name='cadastrar_acabamento'),
    path('cadastrar_papel/', views.cadastrar_papel, name='cadastrar_papel'),
    path('cadastrar_lista_tecnica/', views.cadastrar_lista_tecnica, name='cadastrar_lista_tecnica'),
]
