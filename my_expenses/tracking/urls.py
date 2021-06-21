from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # --- Expenses --- 
    path('getExpenses', views.getExpenses, name='Get for Expenses'), #get all expenses
    path('postExpenses', views.postExpenses),   #post a new expense
    path('deleteExpenses', views.deleteExpenses),   #delete an expense
    # --- Categories ---
    path('getCategories', views.getCategories),   #get all categories
    path('postCategories', views.postCategories),   #post a new category
    path('deleteCategories', views.deleteCategories),   #delete a category
    # --- Cost Frequencies --- 
]
