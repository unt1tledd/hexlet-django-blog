from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name=['hexlet_django_blog', 'article']
    return render(request, 'articles/index.html', context={'name': name})
