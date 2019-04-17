# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<h1>Welcome to my first django project.</h1>")
    return render(request, 'index.html')