from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=26)


class NodeInfo(models.Model):
    knowledgeName = models.CharField(max_length=32)
    relation = models.IntegerField()
    user = models.CharField(max_length=20, null=True)
    favourite = models.IntegerField()
    time = models.DateTimeField(auto_now=True, null=True)


class Link(models.Model):
    source = models.CharField(max_length=26)
    target = models.CharField(max_length=26)
    name = models.CharField(max_length=26)
    user = models.CharField(max_length=20, null=True)
