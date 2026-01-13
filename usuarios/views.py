from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForms


def novo_usuario(request):
    # tipo, validar, informar e salvar
    if request.method == 'POST':
        formulario = UserRegisterForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario =  formulario.cleaned_data.get('username') 
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!' )
            return redirect('investimentos')
    
    else:
        formulario = UserRegisterForms()
        
    return render (request, 'usuarios/novo_usuario.html', {'formulario': formulario})
    

# Create your views here.
