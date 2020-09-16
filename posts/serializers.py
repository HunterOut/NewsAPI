from rest_framework import serializers
from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    '''Новости'''
    comments = serializers.SlugRelatedField(slug_field='author', read_only=True, many=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

################## Not used ######################
class DetailSerializer(serializers.ModelSerializer):
    '''Подробности'''
    comments = serializers.SlugRelatedField(slug_field='author', read_only=True, many=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    '''Добавление комментария'''

    class Meta:
        model = Comment
        fields = '__all__'