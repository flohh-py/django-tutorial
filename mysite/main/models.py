from django.db import models

class Main(models.Model):
    title = models.CharField(max_length=140)
