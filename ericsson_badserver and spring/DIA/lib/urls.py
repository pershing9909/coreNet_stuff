# lib/urls.py
from django.urls import path

from . import views
app_name = 'lib'
urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('addBook/', views.addBook, name='addBook'),
]