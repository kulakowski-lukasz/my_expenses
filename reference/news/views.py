from django.http.response import JsonResponse
from django.shortcuts import render
from news.models import News

# Create your views here.
#zwracamy html
def index(request):
    newsy = News.objects.all().order_by('-posted_date').values()
    context = {'zmienna': list(newsy)}

    return render(request, 'index.html', context)

#zwracamy json
#przegladarka wie ze to nie jest strona tylko response <dostaje naglowek - content type>
def rest_response(request):
    newsy = News.objects.all().order_by('-posted_date')
    response = {'data': []}
    for i in newsy:
        response['data'].append(i.title)

    return JsonResponse(response)
    