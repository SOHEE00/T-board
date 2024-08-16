from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse, get_object_or_404
from .models import *

def index(request) :
    todos = Todo.objects.all()
    texts = Text.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs, 'urls': urls}
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
    todo = Todo.objects.get(id=todo_id)
    todos = Todo.objects.all()
    texts = Text.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs, 'urls': urls,'todo':todo}
    return render(request, 'Table/updatePage.html', content)

def Create_URL(request) :
    content_urls = request.POST['todoURL']
    new_url = CreateUrl(url_content = content_urls)
    new_url.save()

    return HttpResponseRedirect(reverse('index'))


def Delete_url(request) :
    done_url_id = request.GET['urlNum']
    print("완료한 todo의 id", done_url_id)
    done_url = CreateUrl.objects.get(id = done_url_id)
    done_url.delete()

    return HttpResponseRedirect(reverse('index'))

def timesheet(request):
    todos = Todo.objects.all()
    texts = Text.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs, 'urls': urls}
    return render(request, 'Table/timesheet.html', content)

def main(request) :
    return HttpResponseRedirect(reverse('index'))

def loginsheet(request) :
    return render(request,'Table/login.html')