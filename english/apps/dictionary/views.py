from django.views.generic import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer


class WordListView(APIView):
    def get(self, request, format=None):
        data = [word.word for word in Word.objects.all()]
        return Response(data)


class WordDetailView(DetailView):
    model = Word

    def get_object(self):
        word = Word.objects.get(word=self.kwargs['word'])
        return word

    def get_template_names(self):
        if self.request.is_ajax():
            return 'dictionary/word.html'
        else:
            return 'dictionary/word_detail.html'
