from django.db import models

class Post(models.Model):
    text = models.TextField()
    comments = models.CharField(max_length=256)
    email = models.EmailField()

