from django.shortcuts import render
from .models import Memo
from .serializers import MemoSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    def create(self, request):
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        memo = Memo.objects.get(id=request.data['id'])
        memo.delete()

    def update(self, request, pk=None):
        pass

    @action(detail=False, list=True, methods=['POST'])
    def get_content(self, request):
        memo = Memo.objects.get(id=request.data['id'])
        serializer = MemoSerializer(memo)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

# Create your views here.
