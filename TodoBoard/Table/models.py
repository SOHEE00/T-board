from django.db import models 

class Todo(models.Model) :
    content = models.CharField(max_length=255)
    text_content = models.TextField(null=True, blank=True)
    

class Text(models.Model) :
    todo_content = models.TextField()

class CreateUrl(models.Model) :
    url_content = models.CharField(max_length=300)