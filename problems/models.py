from django.db import models

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=255)
    topic = models.CharField(max_length=100, null=True)
    pattern = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, null=True)
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
