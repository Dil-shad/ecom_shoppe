from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.


def SearchResult(request):
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q').lower()
        print(query)
        Products = Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
        print(Products)
        context = {
            'query': query,
            'products': Products,
        }
    return render(request, 'search.html', context)
