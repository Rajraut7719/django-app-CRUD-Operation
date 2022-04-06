from django.db import models

# Create your models here.
class MyUser(models.Model):
  
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=900,default="raj")
    # pub_date = models.DateField(null=True, blank=True)
   
    def __str__(self):
        return f"{self.title}"