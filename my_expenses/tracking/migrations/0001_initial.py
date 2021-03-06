# Generated by Django 3.2.4 on 2021-06-07 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, verbose_name='Nazwa kategorii')),
                ('category_icon', models.ImageField(blank=True, upload_to='icons', verbose_name='Ikonka kategorii')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='CostFreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(max_length=200, verbose_name='Czestotliwosc kosztow')),
                ('is_regular', models.BooleanField(verbose_name='Wydatek regularny')),
            ],
            options={
                'verbose_name': 'Czestotliwosc kosztu',
                'verbose_name_plural': 'Czestotliwosc kosztow',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_date', models.DateField(verbose_name='Data wydatku')),
                ('expense_amount', models.FloatField(verbose_name='Kwota wydatku ')),
                ('comment', models.CharField(max_length=1000, verbose_name='Komentarz')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tracking.category', verbose_name='Kategoria')),
            ],
            options={
                'verbose_name': 'Wydatek',
                'verbose_name_plural': 'Wydatki',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='cost_freq',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tracking.costfreq', verbose_name='Czestotliwosc kosztow'),
        ),
    ]
