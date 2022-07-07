from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text