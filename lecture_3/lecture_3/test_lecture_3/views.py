from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
def index(request):
    context = {
        'title': 'na Kriso saita',
        'person': {
            'first_name': 'Kriso',
            'last_name': 'Omayski'
        },
        'person_class': Person('Kriso', 'Omayski'),
        'names': ['Mimi','Geri','Pesho','Gosho'],
        'ages': [10,20,30,40],
    }

    return render(request,'test_lecture_3/index.html', context)
