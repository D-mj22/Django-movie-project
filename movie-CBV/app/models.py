from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=20,unique=True,primary_key=True)
    desc=models.CharField(max_length=300)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movies/image",null=True,blank=True)

    def __str__(self):
        return self.name
