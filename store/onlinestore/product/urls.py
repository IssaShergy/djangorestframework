from django.urls import path
from .views import  product_list ,product_detail  #ProductDetials,ProductListview
urlpatterns = [
   path("products/",product_list,name="product-list"),
   path("products/<int:pk>/",product_detail,name="product-detials"),
  # path("products/<int:pk>",ProductDetials.as_view(),name="product-detials") 
   
]