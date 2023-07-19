from django.db import models


# Create your models here.

class NodeInfo(models.Model):
    knowledgeName = models.CharField(max_length=32)
    relation = models.IntegerField()


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=26)

