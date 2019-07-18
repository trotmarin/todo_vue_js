from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'

class TodoCV(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')

class TodoLV(ListView):
    models = TodoCV
    template_name = 'todo/todo_list.html'

class TodoDelV(DeleteView):
    modles = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')