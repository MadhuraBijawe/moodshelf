
from django.contrib import admin
from .models import Mood, Book, MoodGenreMap, Favorite

admin.site.register(Mood)
admin.site.register(Book)
admin.site.register(MoodGenreMap)
admin.site.register(Favorite)