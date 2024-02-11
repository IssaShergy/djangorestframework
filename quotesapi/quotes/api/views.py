from rest_framework import generics
from quotes.models import Quote
from quotes.api.serializer import QuoteSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly
class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset=Quote.objects.all().order_by("-1")
    serializer_class=QuoteSerializer
    permission_class=[IsAdminUserOrReadOnly]
class QuoteDetailAPIview(generics.RetriveUpdateDestroyAPIView):
    queryset=Quote.objects.all()
    serializer_class=QuoteSerializer
    permission_class=[IsAdminUserOrReadOnly]
