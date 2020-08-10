from django.db import models

# Create your models here.
class employee (models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    salary = models.IntegerField()