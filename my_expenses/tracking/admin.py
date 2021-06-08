from django.contrib import admin
from .models import CostFreq, Category, Expense

# Register your models here.
@admin.register(CostFreq)
class CostFreqAdmin(admin.ModelAdmin):
    list_display = ('frequency','is_regular')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_icon','cost_freq')

@admin.register(Expense)
class CategoryExpense(admin.ModelAdmin):
    list_display = ('expense_summary', 'expense_date', 'category', 'comment')

    @admin.display(description='Podsumowanie')
    def expense_summary(self, obj):
        return f"{obj.expense_amount}zl z dnia {obj.expense_date} wydane na {obj.category}"