from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, alterar, excluir

urlpatterns = [
    path('', home),
    path('salvar', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('alterar/<int:id>', alterar, name="alterar"),
    path('excluir/<int:id>', excluir, name="excluir")
]
