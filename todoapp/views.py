from django.contrib.auth import authenticate
from django.shortcuts import redirect, get_object_or_404, render
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import *
from .models import *
import datetime

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        todo_items = TodoItem.objects.filter(user=request.user).order_by('-created_at')
        context = {'todoitems': todo_items}
    else:
        context = {'todoitems': []}
    return render(request, 'todo.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url=reverse_lazy('login'))
def addTodo(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        description = (request.POST.get('description') or '').strip()
        dd = (request.POST.get('deadline_date') or '').strip()

        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to add tasks.')
            return redirect('login')

        if not title:
            messages.error(request, 'Please provide a title.')
            return redirect('home')

        if dd:
            try:
                deadline_date = datetime.datetime.strptime(dd, '%Y-%m-%d').date()
            except Exception:
                deadline_date = None
        else:
            deadline_date = None

        item = TodoItem.objects.create(
            user=request.user,
            title=title,
            description=description,
            deadline_date=deadline_date
        )
        messages.success(request, f'Task added: {item.title}')

    return redirect('home')

def deleteTodo(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(TodoItem, id=pk)
        item.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)