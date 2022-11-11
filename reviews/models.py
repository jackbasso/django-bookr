from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The publisher's email address.")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # Many to one relationship
    contributors = models.ManyToManyField('Contributor', through="BookContributor") # through: special field option for an intermediary table

    def __str__(self):
        return self.title

class Contributor(models.Model):
    '''
    A contributor to a Book, e.g. author, editor, co-author.
    '''
    first_names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_names

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book", choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(null=True)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)