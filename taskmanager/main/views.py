from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.order_by('title')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной.'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')