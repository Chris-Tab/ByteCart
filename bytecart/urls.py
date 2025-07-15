from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.contrib import admin


from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('contact/', contact_page, name='contact_page'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('', include('products.urls')),   

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)