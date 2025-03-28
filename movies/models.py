from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.film_adi}'
