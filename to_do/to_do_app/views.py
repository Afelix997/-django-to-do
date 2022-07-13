from django.shortcuts import render, redirect
from django.http import HttpResponse,  JsonResponse
from .models import Todo

def index(request):
    return render(request, 'to_do_app/index.html')
def todo(request):
    if request.method == 'GET':
        return render(request, 'to_do_app/todo.html', { 'context':Todo.objects.all()})

    if request.method == 'POST':
        try:
            data = request.POST
            Todo.objects.create(title=data['title'], desc=data['desc'])
            return render(request, 'to_do_app/todo.html', { 'context':Todo.objects.all()})
        except Exception as error:
            print(str(error))
            return JsonResponse({'success':False})
    
def todo_new(request):
    return render(request, 'to_do_app/todo_new.html')

def get_todo(todo_id):
    return Todo.objects.get(id = todo_id)

def todo_detail(request,todo_id):
    todo_item=get_todo(todo_id)
    return  render(request, 'to_do_app/todo_detail.html', {'item': todo_item})
def todo_edit(request,todo_id):
    todo_item=get_todo(todo_id)
    return  render(request, 'to_do_app/todo_edit.html', {'item': todo_item})
def todo_edit_(request,todo_id):
    data = request.POST
    Todo.objects.filter(id=todo_id).update(title=data['title'], desc=data['desc'])
    return redirect('/todo/')
def todo_delete(request,todo_id):
    data = request.POST
    Todo.objects.filter(id=data['id']).delete()
    return redirect('/todo/')
   