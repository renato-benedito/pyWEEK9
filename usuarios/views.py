from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth



def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=username, password=senha)
 
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/usuarios/login')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/login')


def cadastro(request):
 if request.method == 'GET':
    return render(request, 'cadastro.html')
 else:
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas informadas não coincidem...')
        return redirect('/usuarios/cadastro')
    
    user = User.objects.filter(username=username)
    if user.exists():
        messages.add_message(request, constants.ERROR, 'Usuário já existe...')
        return redirect('/usuarios/cadastro')
    
    try:
        user = User.objects.create_user(
            username=username,
            password=confirmar_senha,
        )

        return redirect('/usuarios/login')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do servidor...')
        return redirect('/usuarios/cadastro')