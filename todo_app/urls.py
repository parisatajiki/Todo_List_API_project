from django.urls import path
from . views import AddTodo , TodoList , TodoDelete,TodoUpdate , TodoFiltterStatus



urlpatterns = [
    path ('add',AddTodo.as_view(),name='add_todo'),
    path ('list',TodoList.as_view(),name='todo_list'),
    path ('delete/<int:pk>',TodoDelete.as_view(),name='todo_delete'),
    path ('update/<int:pk>',TodoUpdate.as_view(),name='todo_update'),
    path ('status',TodoFiltterStatus.as_view(),name='todo_filter'),
]