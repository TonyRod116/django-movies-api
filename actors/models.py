from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    image = models.ImageField(upload_to='actors/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.nationality}'