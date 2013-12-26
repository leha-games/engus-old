from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer


class FlatWordListView(APIView):
    def get(self, request, format=None):
        data = [word.word for word in Word.objects.filter(public=True)]
        return Response(data)


class WordDetailView(RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = "word"
