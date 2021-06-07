from django.urls import path
from quotes.api.views import QuotesCreateAPIView, QuotesDetailAPIView

urlpatterns = [
    path('quotes/', QuotesCreateAPIView.as_view(), name = "quote-list"),
    path('quote/<int: pk>/', QuotesDetailAPIView.as_view(), name = "quote-details")
]