from django import http
from django.shortcuts import render

from lecture_1.tasks.models import Task


# Create your views here.

# def index(request):
#     tasks = Task.objects.all()
#
#     content = "<h1>My site</h1>" + \
#         "<h3>this is my tasks:<h3>"
#
#
#     bebeshki = "Ти си гъз"
#
#     result = [content]
#
#     for t in tasks:
#         result.append(f"""
#         <ul>
#         <li><h2>task: {t.title} </h2>
#         <p>description: {t.description}  </p></li>
#         </ul>
#         """)
#
#     return  render(request, 'tasks/index.html')


def index(request):

    title_filter = request.GET.get('filter',None)
    tasks = Task.objects.all()
    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    tasks_count = tasks.count()

    context={
        "title":"My site",
        "tasks_count":tasks_count,
        "tasks":tasks

    }
    return render(request,
    'tasks/index.html',
                   context)