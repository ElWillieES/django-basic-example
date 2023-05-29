from django.db import models
from django.urls import reverse


class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
