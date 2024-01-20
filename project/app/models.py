from django.db import models

class User(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    # Email = models.EmailField()
    # Passs = models.CharField(max_length=100)
    # Cpass = models.CharField(max_length=100)





# Create your models here.
