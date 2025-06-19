from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookQuerySet(models.QuerySet):
    def published_after(self, year):
        return self.filter(publication_date__year__gt=year)

    def by_author(self, author_name):
        return self.filter(authors__name__icontains=author_name)

    def recent(self):
        return self.order_by('-publication_date')

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    objects = BookQuerySet.as_manager()

    def __str__(self):
        return self.title

    def author_names(self):
        return ", ".join(author.name for author in self.authors.all())

    def was_published_recently(self):
        return self.publication_date >= timezone.now().date()