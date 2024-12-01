from django.urls import path

from lecture_3.test_lecture_3.views import index

urlpatterns = [
    path('', index, name='index'),

]
