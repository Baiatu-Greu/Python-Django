from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.
# index = mainpage of an app


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # aici e ca un try-except block, primul argument e obiectul care are devenii move
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
