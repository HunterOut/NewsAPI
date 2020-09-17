from django_cron import CronJobBase, Schedule

from .models import Post


class ResetPostsUpvotes(CronJobBase):

    RUN_AT_TIMES = ["0:01"]

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "posts.reset_post_upvotes"

    def do(self):
        Post.objects.filter(amount_of_upvotes__gt=0).update(
            amount_of_upvotes=0
        )