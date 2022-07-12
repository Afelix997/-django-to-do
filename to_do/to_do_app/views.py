from django.shortcuts import render
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
        except Exception as e:
            print(str(e))
            return JsonResponse({'success':False})
    
    
def todo_new(request):
    return render(request, 'to_do_app/todo_new.html')
