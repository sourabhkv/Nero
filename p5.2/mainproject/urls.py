from django.contrib import admin
from django.urls import path
from studCourseRegApp.views import enrolledStudentsUsingAjax, generateCSV, home, registerAjax, studentlist,courselist,register,enrolledStudents,add_project,StudentListView,StudentDetailView,generatePDF
urlpatterns = [
    path('secretadmin/', admin.site.urls),
    path('',home),
    path('home/',home),
    path('studentlist/',studentlist),
    path('courselist/',courselist),
    path('register/',register),
    path('enrolledlist/',enrolledStudents),
    path('addproject/',add_project),
    path('genericlistviewstudent/',StudentListView.as_view()),
    path('genericdetailedviewstudent/<int:pk>/',StudentDetailView.as_view()),
    path('download_course_table_as_csv/',generateCSV),
    path('download_course_table_as_pdf/',generatePDF),
    path('courseRegUsingAjax/',registerAjax),
    path('course_search_ajax/',enrolledStudentsUsingAjax),
    
]

