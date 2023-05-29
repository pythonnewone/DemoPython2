# from http.client import HTTPResponse

from django.shortcuts import render



# Create your views here.
def demo(request):
    return HTTPResponse("hello world")