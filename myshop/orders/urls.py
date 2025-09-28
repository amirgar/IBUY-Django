from . import views
from django.urls import re_path 


urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
    re_path(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]