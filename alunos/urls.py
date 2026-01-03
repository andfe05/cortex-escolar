from django.urls import path
from .views import lista_alunos

urlpatterns = [
    path('alunos/', lista_alunos, name='lista_alunos'),
]
