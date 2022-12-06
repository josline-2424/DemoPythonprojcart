from django.urls import path
from . import views

app_name = 'Democartsearchapp'
urlpatterns = [path('', views.SearchResult, name='SearchResult')]
