from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_yr = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.title
    
