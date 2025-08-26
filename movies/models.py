from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(
        to='users.User', # the 'to' argument alolows us toi tell Django which model to this field shopuld be related to
        on_delete=models.CASCADE, # on_delete we can cset CASCADE to delete this object when the relation is deleted. SET_NULL if it's a non-required field
        related_name='owned_movies',
    )
    
    def __str__(self):
        return f'{self.title} ({self.year})'