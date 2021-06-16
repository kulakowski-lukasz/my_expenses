from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getExpenses', views.getExpenses, name='Get for Expenses'),
    path('postStuff', views.postStuff),
]
