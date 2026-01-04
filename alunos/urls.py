from django.urls import path
from .views import (
    lista_alunos,
    criar_aluno,
    editar_aluno,
    excluir_aluno,
    dashboard
)

urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path('dashboard/', dashboard, name='dashboard'),
    path('novo/', criar_aluno, name='criar_aluno'),
    path('editar/<int:id>/', editar_aluno, name='editar_aluno'),
    path('excluir/<int:id>/', excluir_aluno, name='excluir_aluno'),
]
