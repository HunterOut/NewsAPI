from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    '''Комментарии'''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    '''Новости'''

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpvoteView(APIView):
    """Upvotes for post"""

    def get(self, request, post_id):

        post = Post.objects.filter(pk=post_id).first()

        if not post:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND,
            )

        post.upvote()

        return Response({"message": "You successfully upvoted the post!"})