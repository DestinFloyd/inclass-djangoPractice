from django.db import models

# Create your models here.
class Banana(models.Model):
    color = models.TextField()
    name = models.TextField()

    def __str__(self):
        return self.name