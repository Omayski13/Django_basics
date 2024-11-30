from django.urls import path

from lecture_2.departments.views import index, details_department_1, details_department_2, details_department_with_pk, \
    details_department_with_name

urlpatterns = (
    path('', index),
    # path('1/', details_department_1),
    # path('2/', details_department_2),
    path('<int:pk>/', details_department_with_pk),
    path('<str:name>/', details_department_with_name),

)