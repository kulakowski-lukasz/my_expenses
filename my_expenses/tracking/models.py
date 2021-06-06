from django.db import models

# Create your models here.
class CostTypes(models.Model):
    cost_name = models.CharField('Typy kosztow', max_length=200)


class Categories(models.Model):
    category_name = models.CharField('Nazwa kategorii', max_length=200)
    category_icon = models.ImageField('Ikonka kategorii', upload_to='icons', blank=True)
    cost_type = models.OneToOneField(CostTypes, verbose_name="Typy kosztow", on_delete=models.CASCADE)

class Expenses(models.Model):
    expense_date = models.DateField('Data wydatku')
    expense_amount = models.FloatField('Kwota wydatku ')