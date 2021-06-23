from django.db import models
 
class New_Records(models.Model):
    name = models.CharField(max_length=60)
    time = models.DateTimeField(null=True)
    date = models.DateField(null=True)
 
    def __str__(self):
        return self.name 