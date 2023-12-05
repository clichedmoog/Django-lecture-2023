from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artists/') 
    description = models.TextField()

class Album(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='albums/') 
    artist = models.OneToOneField(
        Artist, 
        on_delete=models.CASCADE,
        related_name='album',
    )
    release_date = models.DateField()
    genre = models.CharField(max_length=50)


class Song(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name='songs',
    )
    title = models.CharField(max_length=255)
    duration = models.DurationField()
