from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def home(request):
    '''render the home page'''
    if request.method == 'POST':
        user_input = request.POST.get('user_task')
        new_task = Task()
        new_task.name = user_input
        new_task.save()
    tasks = Task.objects.all()
    return render(request,'users.html',{'tasks':tasks})

def delete_task(request):
    '''remove a task from the database'''
    if request.method == 'POST':
        task_id = request.POST.get('item_to_delete')
        task = Task.objects.get(id=task_id)
        task.delete()
    return redirect('home')
