from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('create-todo/<int:task_id>/', views.create_todo, name='create-todo'),

    # path('append-to-form/<int:pk>/', views.append_to_form, name='append-to-form'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete-task'),
]
