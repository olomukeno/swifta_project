from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    # related_name - the way it is accessed from the related object
    name = models.CharField(max_length=150)
    list_complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # since django doesn't know the type of object that the class ToDoList is since it is an object not defined within
    # django and therefore the foreignkey implies that we would use a todolist object when we create a new item.
    # The on_delete means that since all items exist within a To-Do list when it is deleted, the items disappear as well
    text = models.CharField(max_length=250)
    completed = models.BooleanField()

    def __str__(self):
        return self.text


