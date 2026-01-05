from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from .models import Aluno

@login_required(login_url='login')
def dashboard(request):
    total_alunos = Aluno.objects.count()

    alunos_por_serie = (
        Aluno.objects
        .values('serie')
        .annotate(total=Count('id'))
        .order_by('serie')
    )

    context = {
        'total_alunos': total_alunos,
        'alunos_por_serie': alunos_por_serie,
    }

    return render(request, 'alunos/dashboard.html', context)


from django.shortcuts import render
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()

    nome = request.GET.get('nome')
    serie = request.GET.get('serie')
    turno = request.GET.get('turno')
    ativo = request.GET.get('ativo')

    if nome:
        alunos = alunos.filter(nome__icontains=nome)

    if serie:
        alunos = alunos.filter(serie=serie)

    if turno:
        alunos = alunos.filter(turno=turno)

    if ativo in ['true', 'false']:
        alunos = alunos.filter(ativo=(ativo == 'true'))

    series = Aluno.objects.values_list('serie', flat=True).distinct()
    turnos = Aluno.objects.values_list('turno', flat=True).distinct()

    context = {
        'alunos': alunos,
        'series': series,
        'turnos': turnos,
    }

    return render(request, 'alunos/lista.html', context)


def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos:lista_alunos')  # ✅ AQUI
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
            return redirect('alunos:lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form.html', {'form': form})

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        messages.warning(request, 'Aluno excluído com sucesso!')
        return redirect('alunos:lista_alunos')

    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})

from django.db.models import Count
from .models import Aluno

from .models import Aluno

from django.shortcuts import render
from django.db.models import Count
from .models import Aluno

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('login')
