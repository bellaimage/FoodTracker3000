from django.shortcuts import render
from django.http import HttpResponse

def shoppingList(request):
    return HttpResponse('Shopping List')