from django.db import models


# Create your models here.

class NodeInfo(models.Model):
    knowledgeName = models.CharField(max_length=32)
    relation = models.IntegerField()
