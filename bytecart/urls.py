from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView


from carts.views import cart_home, checkout_home

from accounts.views import guest_register_view, login_page, register_page
from addresses.views import checkout_address_create_view
from .views import home_page, about_page, contact_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/', checkout_home, name='checkout'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('carts/', include("carts.urls"), name='cart'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path("orders/", include("orders.urls", namespace="orders")),
    




    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)