from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from tasks.models import Task
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, "Task created successfully!")
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')