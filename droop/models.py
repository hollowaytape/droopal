from django.db import models

class Tree(models.Model): # table name is droop_tree.
    id = models.IntegerField(primary_key=True)
    threshold = models.IntegerField() # 0 - 255
    
    ripeness = models.BooleanField()
    
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __unicode__(self):
        return self.id
    
class Reading(models.Model): # table name is droop_reading.
    tree = models.ForeignKey(Tree)
    date_time = models.DateTimeField()
    value = models.IntegerField()
    
    def __unicode__(self):
        return "%s-%s-%s" % (self.id, self.hour, self.value)
        
# Verification of ripeness?
# How many readings do we want to store?