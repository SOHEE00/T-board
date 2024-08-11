from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from .models import *

def index(request) :
    todos = Todo.objects.all()
    texts = Text.objects.all()
    content = {'todos':todos, 'texts':texts}
    return render(request,'Table/main.html',content)

def Create_todo(request) :
    todo_content = request.POST['todoTable']
    todo_text = request.POST['todoText']
    new_todo = Todo(content = todo_content)
    new_text = Text(todo_content = todo_text)
    new_todo.save()
    new_text.save()
    
    return HttpResponseRedirect(reverse('index'))

def Todo_delete(request) :
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def Todo_update(request, todo_id) :
    todos = Todo.objects.get(id=todo_id)
    content = {'todos':todos}
    return render(request, 'updateTodo.html', content)