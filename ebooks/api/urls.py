from django.urls import path
from ebooks.api.view import EbookListCreateAPIView

urlpatterns =[
    path('ebooks/', EbookListCreateAPIView.as_view(), name="ebook-list"),
]