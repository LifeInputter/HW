from django.db import models
from django.utils.timezone import timezone


# Create your models here.
class Buyer(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name


class Game(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=250)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # цена(DecimalField)
    size = models.DecimalField(max_digits=10, decimal_places=2)  # описание(неограниченное кол-во текста)
    description = models.TextField(db_default=True)  # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title


class Phones(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(db_default=True)
    year_of_release = models.IntegerField(default=None)

    def __str__(self):
        return self.title
