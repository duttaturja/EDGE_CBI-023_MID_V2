from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_data = models.DateField()
    price  = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    @classmethod
    def calculate_avg_price(cls):
        return Book.objects.aggregate(models.Avg('price'))['price__avg']