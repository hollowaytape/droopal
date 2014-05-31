from django.db import models

class Tree(models.Model):
    id = models.IntegerField(primary_key=True)
    threshold = models.IntegerField()
    ripeness = models.BooleanField()
    
    def __unicode__(self):
        return self.id
    
class Reading(models.Model):
    tree = models.ForeignKey(Tree)
    date_time = models.DateTimeField()
    value = models.IntegerField()
    
    def __unicode__(self):
        return "%s-%s-%s" % (self.id, self.hour, self.value)