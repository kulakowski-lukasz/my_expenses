from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from tracking.models import Expense, Category, CostFreq

# Create your views here.
def index(request):
    return HttpResponse("This is the part of tracking expenses")


# --- Expenses ---

#Get all expenses
def getExpenses(request):
    expenses = Expense.objects.all().order_by('expense_date')
    response = list(expenses.values())
    return JsonResponse(response, safe=False)

#Post an expense
@csrf_exempt 
def postExpenses(request):
    body = json.loads(request.body)
    new_expense = Expense()
    #all expense details
    new_expense.expense_date = body["expense_date"]
    new_expense.expense_amount = body["expense_amount"]
    new_expense.comment = body["comment"]
    
    new_expense_category = Category.objects.get(category_name=body["category"])
    new_expense.category = new_expense_category

    new_expense.save()
    return HttpResponse(status=200)

#Delete an expense
@csrf_exempt 
def deleteExpenses(request):
    body = json.loads(request.body)
    #deleting by expense date
    #TODO: this is not unique way of deletion, this has to be changed
    remov_expense = Expense.objects.get(expense_date=body["expense_date"])
    remov_expense.delete()
    return HttpResponse(status=200)



# --- Categories ---
#Get all categories
def getCategories(request):
    categories = Category.objects.all().order_by('category_name')
    response = list(categories.values())
    return JsonResponse(response, safe=False)

#Post a category
@csrf_exempt 
def postCategories(request):
    body = json.loads(request.body)
    new_category = Category()
    #all expense details
    new_category.category_name = body["category_name"]
    
    new_category_cost_freq = CostFreq.objects.get(frequency=body["cost_freq"])
    new_category.cost_freq = new_category_cost_freq

    new_category.save()
    return HttpResponse(status=200)

#Delete a category
@csrf_exempt 
def deleteCategories(request):
    body = json.loads(request.body)
    #deleting by category name - this should be unique
    remov_category = Category.objects.get(category_name=body["category_name"])
    remov_category.delete()
    return HttpResponse(status=200)


