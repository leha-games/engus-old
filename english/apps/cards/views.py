from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer
from .permissions import IsOwner


class CardViewSet(viewsets.ModelViewSet):
    model = Card
    serializer_class = CardSerializer
    permission_classes = (IsOwner, )
    filter_fields = ('word', )

    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(user=user)

    def pre_save(self, obj):
        obj.user = self.request.user
