"""
URL configuration for TodoBoard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.index, name='index'),
    path('createTodo/',views.Create_todo, name='create_Todo'),
    path('deleteTodo/',views.Todo_delete, name='Todo_Delete'),
    path('updatePage/<int:todo_id>/',views.Todo_update, name='Todo_update'),
    path('createURL/',views.Create_URL, name='create_url'),
    path('deleteurl/',views.Delete_url, name='delete_url'),
    path('timesheet/', views.timesheet, name='timesheet'),
    path('main/', views.main, name='main'),
    path('loginsheet/',views.loginsheet, name='loginsheet'),
]
