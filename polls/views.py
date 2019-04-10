from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse('this is Index page!!!')


def hello(request,foo):
    return HttpResponse('hello world!!! %s' % foo)


def numbers(request,yyy):
    return HttpResponse(yyy)


def sum1(request,x,y):
    sums = x+y
    return HttpResponse(sums)


def i(request):
    # return HttpResponse('iiiiiiiiiii')
    # return HttpResponseRedirect('/polls/index')
    print(reverse('index1'))
    return HttpResponseRedirect(reverse('index1'))