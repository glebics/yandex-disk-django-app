from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.file_list, name='file_list'),
    path('download/', views.download_file, name='download_file'),
    path('download_multiple/', views.download_multiple, name='download_multiple'),
]
