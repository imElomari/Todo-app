from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_todo(request, task_id=None):
    if request.method == 'POST':
        task_name = request.POST.get("task")
        task_description = request.POST.get("description")

        if task_id:
            task = get_object_or_404(Task, id=task_id)
            task.name = task_name
            task.description = task_description
            task.save()
            tasks = Task.objects.all()
            # Render only the updated row
            return render(request, 'task_list.html', {'tasks': tasks, 'updated_task_id': task_id, 'partial': True})

        else:
            Task.objects.create(name=task_name, description=task_description)
            tasks = Task.objects.all()
            # Return full list if it's a new task
            return render(request, 'task_list.html', {'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()

    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# def append_to_form(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return HttpResponse(f'''
#         <input type="hidden" value="{task.id}" name="task_id"/>
#         <input id="name-input" value="{task.name}" placeholder="Enter Task Name" name="task" required/>
#         <input id="description-input" value="{task.description}" placeholder="Enter Task Description" name="description" required/>
#         <button type="submit">Update</button>
#     ''')