from django.db import models

# Create your models here.
class Math(models.Model):
    math1 = models.FloatField()
    math2 = models.FloatField()
    @property
    def result(self):
        return self.math1+ self.math2