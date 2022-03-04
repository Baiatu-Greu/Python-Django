from django.urls import path
from . import views  # . = current directory


# list of path objects that map url endpoints to our view functions
# movies/

app_name = 'movies'

urlpatterns = [
    # cand e empty string = default -> movies/  #we call a reference to the index method
    # initial aveam movies_index, dupa ce setezi numele appului il putem sterge
    path('', views.index, name='index')
    path('<int:movie_id>', views.detail, name='detail')
]
