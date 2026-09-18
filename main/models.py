from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Math(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    math1 = models.FloatField()
    math2 = models.FloatField()
    @property
    def result(self):
        return self.math1+ self.math2

class Profile(models.Model):
    age = models.IntegerField()
    description = models.TextField()
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
