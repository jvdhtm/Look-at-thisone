from django.db import models

class New_Record(models.Model):
    id = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    type = models.IntegerField(blank=True)
    illness = models.IntegerField(null=True)
 
    def __str__(self):
        return self.make + " " + self.model