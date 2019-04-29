from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return HttpResponse('hello world')
def helloworld2():
    return ''

def helloworld3(request):
    return render(request, 'hello.html')