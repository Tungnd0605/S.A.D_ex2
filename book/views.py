from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import book


# Create your views here.

def details(request, id):
    books = book.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
        'book': books,
    }
    return HttpResponse(template.render(context, request))
