from django.shortcuts import render, HttpResponse

def fun(request):
    return  HttpResponse("hello world")

def contact(request):
    return HttpResponse("get contacts from here")


def hello(request, first_name):
    return HttpResponse(f'Hello {first_name}')

def numbers(request,num1, num2):
    return HttpResponse(f'The sum of two numbers are: {num1+num2}')