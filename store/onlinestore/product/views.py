# from django.views.generic.detail import DetailView
# from django.views.generic.list import  ListView
from django.http import JsonResponse
from .models import *

def product_list(request):
    products = Product.objects.all() # [:30]
    data = {"products": list(products.values())} # .values("pk", "name")
    response = JsonResponse(data)
    return response
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
                    "name": product.name,
                    "manufacturer": product.manufacture.name,
                   # "description": product.description,
                    "photo": product.photo.url,
                    "price": product.price,
                    "shipping_cost": product.shipping_cost,
                    "quantity": product.quantity,                   
                }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
            }},
            status=404)
    return response
# class ProductDetials(DetailView):
#     model:Product
#     template_name="product/product_detials.html"
 
# class ProductListview(ListView):
#     model = Product
#     template_name = "product/product_list.html"

 


# Create your views here.
