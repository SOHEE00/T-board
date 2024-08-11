from django.db import models 

class Todo(models.Model) :
    content = models.CharField(max_length=255)
    

class Text(models.Model) :
    todo_content = models.TextField()