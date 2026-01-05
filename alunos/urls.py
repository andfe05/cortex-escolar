from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lista/', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.criar_aluno, name='criar_aluno'),
    path('editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]
