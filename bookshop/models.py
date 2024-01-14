from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AbstractBaseModel(models.Model):
    created_at= models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:abstract = True



class Author(AbstractUser):
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]


    age = models.IntegerField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    gender = models.CharField(max_length = 1, choices = gender_choice, null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Authors'

class Publisher(AbstractBaseModel):
    name = models.CharField(max_length= 58)
    is_active = models.BooleanField(default = False)


class Book(AbstractBaseModel):
    name = models.CharField(max_length= 80)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name = 'books', on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)