from rest_framework import generics,permissions
from ebooks.api.permissions import IsAdminUserOrReadOnly,IsReviewAuthorOrReadOnly
#from rest_framework import mixins
from rest_framework.generics  import get_object_or_404
from   ebooks.api.serializers    import  *
from ebooks.models import Ebook,Review
from rest_framework.exceptions import ValidationError
from ebooks.api.pagination import SmallSetPahination


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset=Ebook.objects.all().order_by("-id")
    serializer_class=EbookSerializer
    permission_class=[IsAdminUserOrReadOnly]
    pagination_class=SmallSetPahination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ebook.objects.all()
    serializer_class=EbookSerializer
    permission_class=[IsAdminUserOrReadOnly]
    
class ReviewCreateAPIView(generics.CreateAPIView):
    queryset=Review.objects.all()
    serializer_class= ReviewSerializer
    permission_class=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self,serializer):
        ebook_pk=self.kwargs.get("ebook_pk")
        ebook=get_object_or_404(Ebook,pk=ebook_pk)
        review_author=self.request.user
        reviewqueryset=Review.objects.filter(Ebook=ebook,review_author=review_author)
        if reviewqueryset.exists():
            raise ValidationError("You Have ALready Reviiew this book")

        serializer.save(Ebook=ebook,review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_class=[IsReviewAuthorOrReadOnly]
    
        



# class EbooklistCreateAPIView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset=Ebook.objects.all()
#     serializer_class=EbookSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)






