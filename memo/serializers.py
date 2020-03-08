from .models import Memo
from rest_framework import serializers

class MemoSerializer(serializers.ModelSerializer):
    published_date = serializers.CharField(read_only=True)
    class Meta:
        model = Memo
        fields = ['id', 'title', 'text', 'published_date']

