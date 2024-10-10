from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from .models import *

def index(request) :
    todos = Todo.objects.all()
    content = {'todos': todos}
    
    return render(request,'Table/main.html',content)

def Create_todo(request) :
    todo_content = request.POST['todoTable']
    todo_text = request.POST['todoText']
    new_todo = Todo(content = todo_content, text_content = todo_text)
    new_todo.save()

    return HttpResponseRedirect(reverse('index'))

def Todo_delete(request) :
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
  
    todo.delete()
    
    return HttpResponseRedirect(reverse('index'))

def Todo_update(request, todo_id) :
    todo = Todo.objects.get(id=todo_id)
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'Table/updatePage.html', content)

def Update_todo(request) :
    todoId = request.POST['todoNum']
    change_todoTable = request.POST['todoTable']
    change_todoText = request.POST['todoText']

    before_todo = Todo.objects.get(id=todoId)
    before_todo.content = change_todoTable
    before_todo.text_content = change_todoText
    before_todo.save()

     # 해당 Todo와 동일한 content를 가진 Star_todo가 있는지 확인 후 업데이트
    
    
    return HttpResponseRedirect(reverse('index'))

def update_modal(request) :
    todoId = request.POST['todo_id']
    todo = Todo.objects.get(id=todoId)
    todo.content = request.POST['todoTable']
    todo.text_content = request.POST['todoText']

     # 파일이 업로드된 경우
    if request.FILES.get('todoImage'):
        image = request.FILES['todoImage']
        file_path = default_storage.save(f'media/todo_images/{image.name}', image)
        todo.image = file_path

    todo.save()

    return HttpResponseRedirect(reverse('index'))







def timesheet(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'Table/timesheet.html', content)

def main(request) :
    return HttpResponseRedirect(reverse('index'))

def loginsheet(request) :
    return render(request,'Table/login.html')


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            # Invalid login credentials
            return render(request, 'Table/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'Table/login.html')


def starpage(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'Table/starpage.html', content)

def sharedpage(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'Table/sharedPage.html', content)


