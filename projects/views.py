from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})


def project_list(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'project_list.html', {'projects': projects})