from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo


def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'base/todo_list.html', context)


def insert_todo_item(request: HttpRequest, ):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/list/')
