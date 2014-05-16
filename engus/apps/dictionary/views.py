from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import viewsets 
from .models import Word, Example
from .serializers import WordSerializer, ExampleSerializer


class FlatWordListView(APIView):

    def get(self, request, format=None):
        data = [word.word for word in Word.objects.all()]
        return Response(data)


class WordDetailView(RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = "word"


class ExampleViewSet(viewsets.ReadOnlyModelViewSet):
    model = Example
    serializer_class = ExampleSerializer
    filter_fields = ('definition', 'definition__word', )

    def get_queryset(self):
        return Example.objects.all()
