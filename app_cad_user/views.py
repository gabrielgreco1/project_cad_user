from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salva os dados inseridos na tela no banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuarios cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)
