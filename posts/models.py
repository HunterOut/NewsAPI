from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    author = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(editable=False, default=0)

    def upvote(self):
        self.amount_of_upvotes += 1
        self.save(force_update=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created"]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    author = models.CharField(max_length=64)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'