from django.db import models

# Create your models here.
class Movie(models.Model):
    image=models.ImageField(upload_to='movie/img',null=True,blank=True)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.title

