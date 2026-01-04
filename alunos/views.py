from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    total_alunos = Aluno.objects.count()

    alunos_por_serie = (
        Aluno.objects
        .values('serie')
        .annotate(total=Count('id'))
        .order_by('serie')
    )

    return render(request, 'alunos/dashboard.html', {
        'total_alunos': total_alunos,
        'alunos_por_serie': alunos_por_serie,
    })


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/form.html', {'form': form})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form.html', {'form': form})

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        messages.warning(request, 'Aluno excluído com sucesso!')
        return redirect('lista_alunos')
    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})

from django.db.models import Count
from .models import Aluno

def dashboard(request):
    total_alunos = Aluno.objects.count()

    alunos_por_serie = (
        Aluno.objects
        .values('serie')
        .annotate(total=Count('id'))
        .order_by('serie')
    )

    return render(request, 'alunos/dashboard.html', {
        'total_alunos': total_alunos,
        'alunos_por_serie': alunos_por_serie,
    })