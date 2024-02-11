from quotes.api.views import QuoteListCreateAPIView,QuoteDetailAPIview
from django.urls import path
urlpatterns = [
    path("quotes/",QuoteListCreateAPIView.as_view,name="quote-list"),
    path("quotes/<int:pk>/",QuoteDetailAPIview.as_view,name="quote-detail")
]