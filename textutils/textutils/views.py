#created by me
from django.http import HttpResponse as HR

def index(request):
    return HR("Hello")

def about(request):
    return HR("About Me")