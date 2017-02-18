from rest_framework import serializers
from nerdz2k17.models import Profile

__author__ = 'abc'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user','college','phone')

