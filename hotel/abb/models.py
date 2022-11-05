from django.db import models

# Create your models here.
class visitors(models.Model):
    name=models.CharField(max_length=20)
    mobile_no=models.IntegerField()
    feedback=models.TextField()