from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .form import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'


class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwarge={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'home.html', {'task1': task1})


def delete(request, taskid):
    if request.method == 'POST':
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = Todoform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})
