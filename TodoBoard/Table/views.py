from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse, get_object_or_404
from .models import *

def index(request) :
    todos = Todo.objects.all()
    texts = Text.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    done = Done_todo.objects.all()  # Done_todo 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs, 'urls': urls, 'done' : done}
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
    texts = Text.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    done = Done_todo.objects.all()  # Done_todo 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs, 'urls': urls,'todo':todo, 'done' : done}
    return render(request, 'Table/updatePage.html', content)

def Update_todo(request) :
    todoId = request.POST['todoNum']
    change_todoTable = request.POST['todoTable']
    change_todoText = request.POST['todoText']
    before_todo = Todo.objects.get(id=todoId)
    before_todo.content = change_todoTable
    before_todo.text_content = change_todoText
    before_todo.save()
    return HttpResponseRedirect(reverse('index'))


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


def mark_as_done(request) :
    todo_id = request.POST['todo_id']
    todo = Todo.objects.get(id=todo_id)
    
    # Done_todo에 데이터 저장
    done_todo = Done_todo(content = todo.content, text_content = todo.text_content)
    done_todo.save()
    
    # 기존 Todo에서 삭제
    todo.delete()
    
    return HttpResponseRedirect(reverse('index'))

def Delete_done(request) :
    done_id = request.GET['doneNum']
    print("완료한 done의 id", done_id)
    doneTodo_id = Done_todo.objects.get(id=done_id)
    doneTodo_id.delete()

    return HttpResponseRedirect(reverse('index'))


def url_update(request, url_id) :
    urls_id = CreateUrl.objects.get(id=url_id)
    todos = Todo.objects.all()
    texts = Text.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    done = Done_todo.objects.all()  # Done_todo 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs, 'urls': urls, 'urls_id':urls_id, 'done' : done}
    return render(request, 'Table/updatePage.html', content)

def Update_url(request) :
    urlId = request.POST['urlNum']
    change_todoUrl = request.POST['todoURL']
    before_url = CreateUrl.objects.get(id=urlId)
    before_url.url_content = change_todoUrl
    before_url.save()
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