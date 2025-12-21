from django.shortcuts import redirect
from django.views.generic import ListView
from .models import *

# Create your views here.
class HomeView(ListView):
    model = TodoItem
    template_name = 'todo.html'
    context_object_name = 'todoitems'

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline_date = request.POST.get('deadline_date') or None

        if title:
            TodoItem.objects.create(
                title=title,
                description=description
            )

        return redirect('home')