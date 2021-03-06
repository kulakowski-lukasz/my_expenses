from django.db import models

# Create your models here.
#Cost frequency - ex monthly, yearly - this is currently a placeholder table, it will be used in a later phase
class CostFreq(models.Model):
    frequency = models.CharField('Czestotliwosc kosztow', max_length=200)
    is_regular = models.BooleanField('Wydatek regularny')

    class Meta:
        verbose_name = "Czestotliwosc kosztu"
        verbose_name_plural = "Czestotliwosc kosztow"

    def __unicode__(self):
        return self.frequency

    def __str__(self):
        return self.frequency


#Categories 
class Category(models.Model):
    category_name = models.CharField('Nazwa kategorii', max_length=200)
    category_icon = models.ImageField('Ikonka kategorii', upload_to='icons', blank=True)
    cost_freq = models.ForeignKey(CostFreq, verbose_name="Czestotliwosc kosztow", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __unicode__(self):
        return self.category_name

    def __str__(self):
        return self.category_name


class Expense(models.Model):
    expense_date = models.DateField('Data wydatku')
    expense_amount = models.FloatField('Kwota wydatku ')
    comment = models.CharField('Komentarz', max_length=1000)
    category = models.ForeignKey(Category, verbose_name="Kategoria", on_delete=models.CASCADE)

    class Meta:
        ordering = ['expense_date']
        verbose_name = "Wydatek"
        verbose_name_plural = "Wydatki"

    def __unicode__(self):
        return f"{self.expense_amount}zl z dnia {self.expense_date} wydane na {self.category}"

    def __str__(self):
        return f"{self.expense_amount}zl z dnia {self.expense_date} wydane na {self.category}"

        