from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('todo-list/', views.todoList, name='todo_list'),
    path('todo-detail/<str:pk>/', views.todoDetail, name='todo_detail'),
    path('todo-create/', views.todoCreate, name='todo_create'),
    path('todo-update/<str:pk>/', views.todoUpdate, name='todo_update'),
    path('todo-delete/<str:pk>/', views.todoDelete, name='todo_delete'),
]