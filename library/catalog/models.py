from typing import get_type_hints
from django.db import models
from django.db.models.deletion import SET_NULL
from django.urls import reverse #used to generate urls by reversing urlpatterns
import uuid

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=200, help_text='enter a book genre')

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)

    #book can have one author but author can have multiple books => foreign key
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='write a short description of the book')

    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='write the 13 digit code')

    #genre can cover many books, and books can have many genres

    genre = models.ManyToManyField(Genre, help_text='select a genre for this book')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #return the url to get detail record of the book
        return reverse('book-detail', args=[str(self.id)])

    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for this particular book')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due back']
    
    def __str__(self):
        #string for representing the Model object
        return f'{self.id} ({self.book.title})'