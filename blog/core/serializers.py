from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    pic = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Profile
        fields = ['name', 'bio', 'pic']


