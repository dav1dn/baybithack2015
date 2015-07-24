from django.contrib.auth import User
from django.db import models


class Hacker(models.Model):

    TSHIRT_SIZE_CHOICES = (
        ('extra small', "Adult Extra Small"),
        ('small', "Adult Small"),
        ('medium', "Adult Medium"),
        ('large', "Adult Large"),
        ('extra large', "Adult Extra Large"),
    )

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=254)
    email = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    tshirt_size = models.CharField(max_length=30, choices=TSHIRT_SIZE_CHOICES)
    vegetarian = models.BooleanField(default=False)
    source = models.CharField(max_length=256)
