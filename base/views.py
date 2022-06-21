from django.shortcuts import render
from django.http import HttpResponse


def list_todo_items(request):
    return render(request, 'base/todo_list.html')
