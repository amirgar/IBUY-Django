from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.urls import re_path 

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'about_us/', include(('about_us.urls', 'about_us'), namespace='about_us')),
    re_path(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    re_path(r'^cart/', include(('cart.urls', "cart"), namespace='cart')),
    re_path(r'^', include(('shop.urls', 'shop'), namespace='shop')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
