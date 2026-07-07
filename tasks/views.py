from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_board')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_board(request):
    todo_tasks = Task.objects.filter(status='To Do')
    inprogress_tasks = Task.objects.filter(status='In Progress')
    completed_tasks = Task.objects.filter(status='Completed')

    context = {
        'todo_tasks': todo_tasks,
        'inprogress_tasks': inprogress_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'task_board.html', context)


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')