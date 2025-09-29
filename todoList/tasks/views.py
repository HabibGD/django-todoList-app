from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import request
from .models import TaskTodo
from .forms import NewTaskForm

# Create your views here.



def index(request):
   tasks = TaskTodo.objects.all()
   
   
   return render(request, "tasks/index.html", {
      "tasks": tasks
   })

def add(request):
    form = NewTaskForm(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('index')
    
    return render(request, "tasks/add.html", {
        "form": form
    })

def update(request, id):
    
    task = get_object_or_404(TaskTodo, id=id)
    form = NewTaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, "tasks/add.html", {
        "form": form
    })

def delete(request, id):
    
    task = get_object_or_404(TaskTodo, id=id)

    if request.method == "POST":
        task.delete()
        return redirect('index')
    return render(request, "tasks/delete.html", {
        "task": task
    })

    
