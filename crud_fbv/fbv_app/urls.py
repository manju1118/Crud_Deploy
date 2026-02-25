from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page, name='home'),
    path('student/create/',views.student_creation,name='create'),
    path('student/detail/<int:stu_id>/',views.student_detail,name='student_detail'),
    path('student/update/<int:stu_id>/',views.student_update,name='update'),
    path('student/delete/<int:stu_id>/',views.student_delete,name='delete'),
]