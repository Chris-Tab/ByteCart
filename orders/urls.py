from django.urls import path
from .views import order_process_view, order_success_view


app_name = 'orders'

urlpatterns = [
    path('process/', order_process_view, name='process'),
    path('success/', order_success_view, name='success'),
]
