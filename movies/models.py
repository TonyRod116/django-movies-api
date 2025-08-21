from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} ({self.year})'