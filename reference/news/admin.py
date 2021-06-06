from news.models import Category
from django.contrib import admin
from news.models import Category, News 

# Register your models here.
#Wewnętrzna metoda panelu admina - przetwarza model na aplikacje w panelu admina
# admin.site.reigster(Category)
# admin.site.register(News)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)