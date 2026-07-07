from django.shortcuts import render, redirect
from .forms import CommentForm


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})