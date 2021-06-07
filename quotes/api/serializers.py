# from rest_framework import serializers
from quotes import Quotes
from rest_framework import serializers
class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = "__all__"    

