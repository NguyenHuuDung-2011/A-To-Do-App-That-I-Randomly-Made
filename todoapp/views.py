from django.shortcuts import redirect, get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import *
import datetime

# Create your views here.
def home(request):
    todo_items = TodoItem.objects.all().order_by('-created_at')
    context = {'todoitems': todo_items}
    return render(request, 'todo.html', context)

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