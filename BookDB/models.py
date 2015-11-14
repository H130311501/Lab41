from django.db import models
class Author(models.Model):
    AuthorID=models.CharField(max_length=30)
    Name=models.CharField(max_length=40)
    Age=models.CharField(max_length=10)
    Country=models.CharField(max_length=50)
    def __unicode__(self):
        return self.AuthorID
        
class Book(models.Model):
    ISBN=models.CharField(max_length=20)
    Title=models.CharField(max_length=100)
    AuthorID=models.CharField(max_length=50)
    Authorname=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    Publicationdate=models.DateField()
    Price=models.CharField(max_length=20)
    def __unicode__(self):
        return self.ISBN
    class Meta:
        ordering=['ISBN']
        

    

# Create your models here.
