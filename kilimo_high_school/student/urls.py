from django.urls import path
from . import views
from.views import create_stream, delete_stream,
urlpatterns = [
    path('', views.student_list, name='base'),
    path('streams/', views.stream_list, name='list_streams'),
    path('streams/<int:pk>/', views.stream_detail, name='stream_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('create/', create_stream, name='create_stream'),
    path('delete/<int:stream_id>/', delete_stream, name='delete_stream'),
]