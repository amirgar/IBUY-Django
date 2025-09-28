from django.shortcuts import render
from shop.models import *

def search(request): 
    model = Product
    return render(request,
                'shop/search_results.html',
                {
                    'object_list': model.objects.filter()
                }
                )
