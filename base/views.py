from django.shortcuts import render
from django.http import HttpResponse


def list_todo_items(request):
    return HttpResponse('from list_todo_items')
