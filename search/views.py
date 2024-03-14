from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from book.models import book
from django.db.models import Q

def index(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = book.objects.filter(
            Q(title__icontains=query)
        ).values()
    else:
        books = book.objects.all().values()

    template = loader.get_template('search.html')
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))