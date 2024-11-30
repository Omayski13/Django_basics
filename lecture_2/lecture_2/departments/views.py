import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse(f"Response from {time.time()}")

def details_department_1(request):
    return HttpResponse(f"Department 1")
def details_department_2(request):
    return HttpResponse(f"Department 2")

def details_department_with_pk(request, pk):
    return HttpResponse(f"Department with pk: {pk}")
def details_department_with_name(request, name):
    return HttpResponse(f"Department with name: {name}")

