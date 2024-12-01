from django.shortcuts import render, redirect
from .models import Aluno

def home(request):
    alunos = Aluno.objects.all()
    return render(request, "index.html", {"alunos": alunos})

def salvar(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    cpf = request.POST.get("cpf")

    Aluno.objects.create(nome=nome, email=email, cpf=cpf)
    alunos = Aluno.objects.all()
    return render(request, "index.html", {"alunos": alunos})

def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, "update.html", {"aluno": aluno})

def alterar(request, id):
    novoNome = request.POST.get("nome")
    novoEmail = request.POST.get("email")
    novoCPF = request.POST.get("cpf")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = novoNome
    aluno.email = novoEmail
    aluno.cpf = novoCPF
    aluno.save()
    return redirect(home)

def excluir(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect(home)