from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link = models.URLField()
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True)
    #upvotes

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'