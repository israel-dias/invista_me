from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def investimentos(request):
    dados = {
        'dados' : Investimento.objects.all() # Quero que vc vá até a tabela Investimentos no banco de dados e retorne todos os objetos
    }
    return render(request, 'investimentos/investimentos.html', context = dados)

@login_required
def detalhes(request, id_investimento):
    dados = {
        'dados' : Investimento.objects.get(pk = id_investimento)
    }
    return render (request, 'investimentos/detalhes.html', dados)

@login_required
def criar (request):
    if request.method == 'POST': # Se por acaso ele for postar, então:
        investimento_form = InvestimentoForm(request.POST) # cria uma variável POST
        if investimento_form.is_valid(): # Se for válido, então ele deve salvar
            investimento_form.save()
        return redirect('investimentos') # Redirecione para a página incial de investimentos
    else: # Se não, então crie um novo investimento
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario' : investimento_form
        }
        return render(request, 'Investimentos/novo_investimento.html', context= formulario)
    
@login_required    
def editar(request,id_investimento):
    investimento = Investimento.objects.get(pk = id_investimento)
    # Novo investimento/1 -> GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance = investimento)
        return render (request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # Caso a requisição seja POST
    else: 
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect ('investimentos')
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk = id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item' : investimento})