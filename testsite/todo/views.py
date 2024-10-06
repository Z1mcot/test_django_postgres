from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title, user=request.user)  # Assign task to the logged-in user
        return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user == request.user:  # Ensure users can only delete their own tasks
        task.delete()
    return redirect('task_list')