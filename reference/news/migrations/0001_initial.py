# Generated by Django 3.2.4 on 2021-06-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa Kategorii')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Odnośnik')),
                ('icon', models.ImageField(blank=True, upload_to='icons', verbose_name='Ikonka Kategorii')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')),
                ('text', models.TextField(verbose_name='Treść')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('categories', models.ManyToManyField(to='news.Category', verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Wiadomość',
                'verbose_name_plural': 'Wiadomości',
            },
        ),
    ]
