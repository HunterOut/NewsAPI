from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from .views import CommentViewSet, PostUpvoteView, PostViewSet


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    """Mixin class for nested routing"""


urlpatterns = [
    path("posts/<int:post_id>/upvote/", PostUpvoteView.as_view()),
]

router = NestedDefaultRouter()

authors_router = router.register("posts", PostViewSet)
authors_router.register(
    "comments",
    CommentViewSet,
    basename="posts-comments",
    parents_query_lookups=["post"],
)

urlpatterns += [
    path(r"", include(router.urls)),
]