from rest_framework import generics, viewsets
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsOwner


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner, ]
    model = Profile

    def get_queryset(self):
        user = self.request.user
        Profile.objects.get_or_create(user=user)
        return Profile.objects.filter(user=user)
