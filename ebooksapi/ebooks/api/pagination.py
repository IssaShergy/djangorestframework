from rest_framework.pagination import  PageNumberPagination

class SmallSetPahination(PageNumberPagination):
    page_size=3