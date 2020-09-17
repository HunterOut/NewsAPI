from rest_framework import serializers
from .models import Comment, Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    '''Добавление комментария'''
    #author = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    '''Новости'''
    #comments = CommentSerializer(many=True)
    #author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "link", "created", "amount_of_upvotes", "author"]