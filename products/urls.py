from django.urls import path

from .views import (
    ProductListView,        
    ProductDetailSlugView,       
)

urlpatterns = [  
    path('products/', ProductListView.as_view(), name='product_list_cbv'),   
    path('products/<slug:slug>/', ProductDetailSlugView.as_view(), name='product_detail_slug'),
]
