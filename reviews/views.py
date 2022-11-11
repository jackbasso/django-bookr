from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

'''
def welcome_view(request):
    message = f"<html><h1>Welcome Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)
'''
def welcome_view(request):
    return render(request, 'base.html')