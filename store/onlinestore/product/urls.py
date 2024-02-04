from django.urls import path
from .views import  product_list ,product_detail,manufacturer_list ,manufacturer_detail #ProductDetials,ProductListview
urlpatterns = [
   path("products/",product_list,name="product-list"),
   path("products/<int:pk>/",product_detail,name="product-detials"),
   path("manufacturers/", manufacturer_list, name="manufacturer-list"),
   path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer-detail")
  # path("products/<int:pk>",ProductDetials.as_view(),name="product-detials") 
   
]