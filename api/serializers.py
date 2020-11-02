from .models import User, Activity, MovieRecomment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class MovieSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = MovieRecomment
        fields = '__all__'