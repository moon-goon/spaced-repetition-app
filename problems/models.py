from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=255)
    problem_statement = models.CharField(max_length=500, blank=True)
    hint = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    pattern = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255)
    ranking = models.IntegerField(null=True, blank=True)
    begin_date = models.DateField(null=True, blank=True)
    repetition_1 = models.DateField(null=True, blank=True)
    repetition_2 = models.DateField(null=True, blank=True)
    repetition_3 = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.begin_date:
            self.repetition_1 = (self.begin_date + timedelta(days=3)).strftime('%Y-%m-%d')
            self.repetition_2 = (self.begin_date + timedelta(days=6)).strftime('%Y-%m-%d')
            self.repetition_3 = (self.begin_date + timedelta(days=13)).strftime('%Y-%m-%d')
            
        super(Problem, self).save(*args, **kwargs)
            