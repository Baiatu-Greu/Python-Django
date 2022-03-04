from django.contrib import admin
from .models import Genre, Movie  # . se refera la current folder

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    # ce sa fie listat cand intri in genre pannel in admin
    list_display = ('id', 'name')  # override


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_creates', )
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
