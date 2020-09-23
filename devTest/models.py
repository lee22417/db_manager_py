from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateTimeField()