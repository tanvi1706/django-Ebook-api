from rest_framework import generics

from Quotes.models import Quotes
from quotes.api.serializers import QuotesSerializer
from quotes.api.permission import IsAdminUserOrReadOnly
from quotes.api.pagination import smallsetPagination

class QuotesCreateAPIView(generics.ListCreateAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = smallsetPagination

class QuotesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
