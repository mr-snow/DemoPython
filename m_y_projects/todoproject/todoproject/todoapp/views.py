from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')

class Task_detail_view(DetailView):
    model = Task
    template_name = 'detail.html'
    app_name='todoapp'
    context_object_name = 'task'

class Task_list_view(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_key'

class Task_Update(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail', kwargs={'pk': self.object.id})

def home(request):
    task_value = Task.objects.all()
    if request.method == 'POST':
        name_1 = request.POST.get('task', '')
        priority_1 = request.POST.get('priority', '')
        date_1 = request.POST.get('date', '')
        task = Task(name=name_1, priority=priority_1, date=date_1)
        task.save();
    return render(request, "home.html", {'task_key': task_value})

def update(request, id):
    task_l = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task_l)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task_l': task_l})

def delete(request, taskid):
    task_del = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task_del.delete();
        return redirect('/')
    return render(request, 'delete.html')

