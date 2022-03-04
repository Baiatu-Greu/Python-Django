from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


# Create your models here.
# RESTfull API- a bunch of conventions that establish how applications should talk to eachother over httpprotocol

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  # return a query(lazy loading)
        resource_name = 'movies'  # how our endpoint will look like
        excludes = ['date_created']
