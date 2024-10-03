from django.db import models 

class Todo(models.Model) :
    content = models.CharField(max_length=255)
    text_content = models.TextField(default='')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='todo_image')

class Text(models.Model) :
    todo_content = models.TextField()

class CreateUrl(models.Model) :
    url_content = models.CharField(max_length=300)

class Done_todo(models.Model):
    content = models.CharField(max_length=255)
    text_content = models.TextField()

class Star_todo(models.Model) :
    content = models.CharField(max_length=255)
    text_content = models.TextField(default='')
   
