from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
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
    if Star_todo.objects.filter(content=todo.content).exists():
        Star_todo.objects.filter(content=todo.content).delete()
    todo.delete()
    
    return HttpResponseRedirect(reverse('index'))

def Todo_update(request, todo_id) :
    todo = Todo.objects.get(id=todo_id)
    todos = Todo.objects.all()
    texts = Text.objects.all()
    done = Done_todo.objects.all()  # Done_todo 모델의 데이터를 가져옴
    todo_text_pairs = zip(todos, texts)
    content = {'todo_text_pairs': todo_text_pairs,'todo':todo, 'done' : done}
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
    
    star_todo = Star_todo.objects.get(id=todoId)
    star_todo.content = before_todo.content
    star_todo.text_content = before_todo.text_content
    star_todo.save()
    
    
    return HttpResponseRedirect(reverse('index'))

def update_modal(request) :
    todoId = request.POST['todo_id']
    todo = Todo.objects.get(id=todoId)
    todo.content = request.POST['todoTable']
    todo.text_content = request.POST['todoText']
    

     # 파일이 업로드된 경우
    if request.FILES.get('todoImage'):
        image = request.FILES['todoImage']
        file_path = default_storage.save(f'todo_images/{image.name}', image)
        todo.image = file_path

    todo.save()

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

def mark_as_star(request) :
    todo_id = request.POST['todo_id']
    todo = Todo.objects.get(id=todo_id)
    # content와 text_content를 기준으로 Star_todo 객체를 생성 또는 검색
    star_todo, created = Star_todo.objects.get_or_create(
        content=todo.content,
        defaults={'text_content': todo.text_content}
    )

    # 객체가 새로 생성되지 않은 경우(이미 존재하는 경우)에는 text_content를 업데이트
    if not created:
        star_todo.text_content = todo.text_content
        star_todo.save()

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
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    done = Done_todo.objects.all()  # Done_todo 모델의 데이터를 가져옴
    content = {'todos': todos, 'urls': urls, 'done':done}
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
    todos = Star_todo.objects.all()
    content = {'todos': todos}
    return render(request, 'Table/starpage.html', content)

def sharedpage(request):
    todos = Todo.objects.all()
    urls = CreateUrl.objects.all()  # CreateUrl 모델의 데이터를 가져옴
    done = Done_todo.objects.all()  # Done_todo 모델의 데이터를 가져옴
    content = {'todos': todos, 'urls': urls, 'done':done}
    return render(request, 'Table/sharedPage.html', content)


def Delete_Star(request) :
    done_star = request.GET['todo_id']
    print("완료한 todo의 id", done_star)
    delete_star = Star_todo.objects.get(id = done_star)
    delete_star.delete()

    return HttpResponseRedirect(reverse('starpage'))