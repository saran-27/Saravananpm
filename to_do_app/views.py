from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully ✅")  # 🔔 Trigger alert
            return redirect('/')

    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    messages.info(request, f"Task '{task.title}' status updated 🔄")  # 🔔 Trigger alert
    return redirect('/')


def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f"Task '{task.title}' updated successfully ✏️")  # 🔔 Trigger alert
            return redirect('/')

    return render(request, 'edit.html', {'form': form})


def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    messages.error(request, "Task deleted ❌")  # 🔔 Trigger alert
    return redirect('/')
