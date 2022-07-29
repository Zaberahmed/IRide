
from django.db import models

# Create your models here.


class Rider(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Weight = models.IntegerField()
    # Sessions

    def _str_(self):
        return self.Name
