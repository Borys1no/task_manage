from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {
        'tasks': tasks
    })

@login_required
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


@login_required

def task_edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task/task_edit.html', {'form':form})
    

@login_required

def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return redirect('task_list')

    