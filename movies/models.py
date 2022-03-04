from django.db import models
from django.utils import timezone

# Create your models here.

# da inherit unui obiect ce automat are metodele pentru a fii incorporat intr un db si tot asa


class Genre(models.Model):
    # models are o tona de instances of field classes- ca intr un database
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):  # we inherit the models class that gives us a ton of methods and stuff to update, delete etc .. stuff from the db
    title = models.CharField(max_length=255)
    release_years = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # ForeignKey ca si la sql db
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_creates = models.DateTimeField(default=timezone.now)
