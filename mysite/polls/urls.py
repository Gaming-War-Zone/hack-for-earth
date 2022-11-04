from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
]