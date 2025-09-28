from django.shortcuts import render

def about(request):
    return render(request, 'shop/about_us.html')