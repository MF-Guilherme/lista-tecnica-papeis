from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar_ciclo/', views.cadastrar_ciclo, name='cadastrar_ciclo'),
]
