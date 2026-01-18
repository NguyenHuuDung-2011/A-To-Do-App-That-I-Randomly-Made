from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from .models import *
import datetime

# Create your views here.
class HomeView(ListView):
    model = TodoItem
    template_name = 'todo.html'
    context_object_name = 'todoitems' 

def addTodo(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    deadline_date = request.POST.get('deadline_date') or None
    if deadline_date is None: deadline_date = datetime.date.today()

    if title:
        TodoItem.objects.create(
            title=title,
            description=description,
            deadline_date=deadline_date
        )

    return redirect('home')
    
def deleteTodo(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(TodoItem, id=pk)
        item.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)