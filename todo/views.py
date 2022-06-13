from django.shortcuts import render

from .models import Post


def todo_list(request):
    todos = Post.objects.all()
    return render(request, 'todo/todo-list.html', {'todos': todos})
