from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password = senha)

    if not user:
         messages.error(request, 'Usuário ou senha inválidos!')
         return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso!')
        return redirect('dashboard')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    # Validação de campos do formulário
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha) <6:
        messages.error(request, 'Senha precisa de 6 caracteres ou mais!')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'As senhas não correspondem!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username = usuario).exists():
        messages.error(request, 'Nome de usuário já existente!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email = email).exists():
        messages.error(request, 'Email já cadastrado!')
        return render(request, 'accounts/cadastro.html')

    messages.success(request,'Conta criada com sucesso!Faça o Login!')
    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name = nome,
                                    last_name = sobrenome)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
