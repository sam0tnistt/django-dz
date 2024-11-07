from django.db import models

class CatFood(models.Model):
    taste = models.CharField(max_length=100)

    def __str__(self):
        return f"CatFood with taste: {self.taste}"

class Cat(models.Model):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
    ]

    MOOD_CHOICES = [
        ('good', 'Good'),
        ('bad', 'Bad'),
        ('sleepy', 'Sleepy'),
    ]

    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    age = models.PositiveIntegerField()
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    owner = models.CharField(max_length=100, blank=True, null=True)

    def purr(self):
        return "Purrr!"

    def scratch(self):
        return "Scratch!"

    def feed(self, cat_food):
        return f"Eating cat food with {cat_food.taste} taste!"

    def __str__(self):
        return f"Cat - Color: {self.color}, Age: {self.age}, Mood: {self.mood}"
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Model2

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#model 3
# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    text = models.TextField()  # Текст поста
    created_date = models.DateTimeField(default=timezone.now)  # Дата створення
    published_date = models.DateTimeField(blank=True, null=True)  # Дата публікації
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор поста

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#видалимо все звідси та запишемо наступний код:
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
