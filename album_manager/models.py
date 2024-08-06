from django.db import models

# Create your models here.
class Artist(models.Model):
    name_artist = models.CharField(max_length=30, null=False)
    origin_country = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.name_artist
    
class Album(models.Model):
    name_album = models.CharField(max_length=30, null=False)
    release_year = models.IntegerField(null=False)
    genre = models.CharField(max_length=30, null=False)
    artist = models.ForeignKey(Artist, on_delete= models.CASCADE)
    picture = models.ImageField(upload_to='album_images')
    
    def __str__(self) -> str:
        return self.name_album
    

    