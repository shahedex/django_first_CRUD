from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=2048)

"""
    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content
"""