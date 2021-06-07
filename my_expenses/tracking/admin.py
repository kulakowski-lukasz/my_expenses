from django.contrib import admin
from .models import CostFreq, Category, Expense

# Register your models here.
admin.site.register(CostFreq)
admin.site.register(Category)
admin.site.register(Expense)
