from django.shortcuts import render, redirect
from .forms import RegisterForm
from projects.models import Project
from tasks.models import Task


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def dashboard(request):

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    todo_tasks = Task.objects.filter(status='To Do').count()

    completed_tasks = Task.objects.filter(status='Completed').count()

    context = {

        'total_projects': total_projects,

        'total_tasks': total_tasks,

        'todo_tasks': todo_tasks,

        'completed_tasks': completed_tasks,

    }

    return render(request, 'dashboard.html', context)