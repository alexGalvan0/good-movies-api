from rest_framework import serializers
from .models import User, Movie, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'plot',
            'cast',
            'poster',
            'rated',
            'director',
            'date_released',
            'imdbId',
            'year',
            'run_time',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = ['user', 'movie', 'review']

class SimpleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')
