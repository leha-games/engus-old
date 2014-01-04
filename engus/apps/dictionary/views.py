from django.db.models import Q
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Word, Example
from .serializers import WordSerializer, ExampleSerializer


class FlatWordListView(APIView):
    def get(self, request, format=None):
        data = [word.word for word in Word.objects.filter(is_public=True)]
        return Response(data)


class WordDetailView(RetrieveAPIView):
    queryset = Word.objects.filter(is_public=True)
    serializer_class = WordSerializer
    lookup_field = "word"


class ExampleViewSet(ModelViewSet):
    model = Example
    serializer_class = ExampleSerializer
    filter_fields = ('definition', 'definition__word', )

    def get_queryset(self):
        user = self.request.user
        return Example.objects.filter(Q(user=user) | Q(is_public=True))

    def pre_save(self, obj):
        obj.user = self.request.user
