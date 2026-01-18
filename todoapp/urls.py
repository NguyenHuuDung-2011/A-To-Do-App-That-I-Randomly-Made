from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', addTodo, name='add-todo'),
    path('delete/<int:pk>/', deleteTodo, name='delete-todo'),
]