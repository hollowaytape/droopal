from django.db import models

class Tree(models.Model):
    id = IntegerField()
    threshold = IntegerField()
    ripeness = BooleanField()
    
class Reading(models.Model):=
    id = models.ForeignKey(Tree)
    value = models.IntegerField()
    hour = models.DateTimeField()