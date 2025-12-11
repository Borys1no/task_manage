from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks
    })


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task list')
    else:
        form = TaskForm()
    return render(request, 'task/task_create.html',{
        'form': form
    })
