from django.db import models

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    GENRE_CHOICES = [
        ('POL', 'Politics'),
        ('SOC', 'Social'),
        ('TRA', 'Travel'),
        ('MUS', 'Music'),
        ('EDU', 'Educational'),
        ('THR', 'Thriller'),
        ('SPO', 'Sports'),
        ('CIN', 'Cinema')
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='blogs')
    publication_date = models.DateField()
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='TRA')
    post = models.ManyToManyField(Post, related_name="posts")

    def __str__(self):
        return self.title