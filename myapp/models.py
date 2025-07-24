from django.db import models
from django.contrib.auth.models import User

class Mood(models.Model):
    name = models.CharField(max_length=50)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emoji} {self.name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class MoodGenreMap(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.mood.name} → {self.genre}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} ❤ {self.book.title}"

class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood.name} @ {self.timestamp}"
