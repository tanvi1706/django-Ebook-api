from django.db import models

class Quotes(models.Model):
    quote_author = models.CharField(max_length=15),
    quote_body = models.CharField(max_length=20),
    context = models.CharField(max_length=10),
    source = models.CharField(max_length=15),
    created_at = models.DateTimeField(auto_now_add=True),
    