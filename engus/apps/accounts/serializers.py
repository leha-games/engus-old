from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.Field(source='user.username')

    class Meta:
        model = Profile
        fields = ('id', 'is_english_mode', 'paid_till', 'username' )
        read_only_fields = ('id', 'paid_till', )
