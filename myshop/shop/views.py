from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Q # новый
from django.views.generic import TemplateView, ListView


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   })

 
def search(request): 
    query = request.GET.get('q')
    object_list = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query) | Q(name=query)
    )
    return render(request,
                'shop/search_results.html',
                {
                    'products': object_list,
                    'counter': len(object_list)
                })



# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/detail.html', {'cart': cart})