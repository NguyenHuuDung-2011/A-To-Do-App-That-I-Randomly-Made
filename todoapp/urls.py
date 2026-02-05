from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout', logoutPage, name='logout'),
    path('add/', addTodo, name='add-todo'),
    path('delete/<int:pk>/', deleteTodo, name='delete-todo'),
]