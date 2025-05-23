from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

''' The Genre Model'''
class Genre(models.Model):
    name = models.CharField(max_length=200, 
                            unique=True, 
                            help_text="Need a book genre (Sci-Fi, Poetry, etc.) to operate! ")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

class Meta:
    constraints = [
        UniqueConstraint(
            Lower('name'),
            name='genre_name_case_insensitive_unique',
            violation_error_message="Error Code 983: Case Insenstive Match - genre already exists"
        )
    ]
  

'''The Language Model'''
class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])
    
'''The Book Model'''
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(max_length=1000, help_text="Give me a brief description of the book: ")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13-Character-Style <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(
        Genre, help_text="Give me the genre for this book: ")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
         return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'
    
    '''The BookInstance Model'''
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="I need to have the book's Unique ID so that I could search the whole library for it. ")
    book = models.ForeignKey('Book', on_delete = models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance in progress'),
        ('o', 'Book on Loan'),
        ('a', 'Available for reading'),
        ('r', 'Reserved for someone else')
        )
    status = models.CharField(
            max_length=1,
            choices=LOAN_STATUS,
            blank=True,
            default='m',
            help_text='Is the book available? '
        )

    class Meta:
            ordering = ['due_back']
            permissions = (("can_mark_returned", "Set book as returned"),)
        
    def __str__(self):
            return f'{self.id} ({self.book.title})'
        
    '''The Author Model'''
class Author(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     date_of_birth = models.DateField(null=True, blank=True)
     date_of_death = models.DateField('Died', null=True, blank=True)

     class Meta:
          ordering = ['last_name', 'first_name']
    
     def get_absolute_url(self):
          return reverse('author-detail', args=[str(self.id)])
     
     def __str__(self):
          return f'{self.first_name}, {self.last_name}'