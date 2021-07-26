from django.shortcuts import render
from django.http import HttpResponse


def project(request):
    return HttpResponse('this is home page')


def projects(request, pk):
    return HttpResponse('this is a redirect from home page to page no :' + str(pk))
