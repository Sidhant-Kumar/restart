from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': 'ecommerce website',
        'description': 'A fully functional website'
    },
    {
        'id': '2',
        'title': 'portfolio website',
        'description': 'A personal website to write articles and display data'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'open source project for community'
    }
]


def project(request):
    context = {'projects': projectList}
    return render(request, 'projects\project.html', context)


def projects(request,pk):
    projectObject = None

    for i in projectList:
        if i['id'] == str(pk):
            projectObject = i
    return render(request, 'projects\second.html',{'project':projectObject})
