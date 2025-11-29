from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse 

# Create your views here.

def home(request): 
    # Vamos retornar a resposta HTTP mais simples: um texto HTML 
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def home2(request): 
    # Vamos retornar a resposta HTTP mais simples: um texto HTML 
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST': 
        tarefa.concluida = True 
        tarefa.save() 
    return redirect('home')

def deletar_tarefa(request, pk): 
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST': 
        tarefa.delete() 
    return redirect('home') 
