from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    edad = models.IntegerField(default=18)

class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class MovieRecomment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField(max_length=100)
    runtime = models.IntegerField()

class User_Activity(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    rating = models.IntegerField()

