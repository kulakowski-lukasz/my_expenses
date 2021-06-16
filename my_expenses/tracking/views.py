from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from tracking.models import Expense

# Create your views here.
def index(request):
    return HttpResponse("This is the part of tracking expenses")

#Get all expenses
def getExpenses(request):
    expenses = Expense.objects.all().order_by('expense_date')
    response = list(expenses.values())
    return JsonResponse(response, safe=False)


#Get expense by date
def getExpenseDate(request)
    pass

def postStuff(request):
    print(request) 
    return HttpResponse()

    # response = {'data': []}
    # for i in expenses:
    #     response['data'].append(i)
    
    