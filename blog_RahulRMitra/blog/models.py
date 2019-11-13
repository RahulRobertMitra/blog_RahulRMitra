from django.db import models


class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each saver models here.

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Represents a blog post
    """
    Post = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=50)
    Text = models.TextField()
    Approved =models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each saver models here.

    def __str__(self):
        return self.Post


    class Meta:
        ordering = ['-created']
