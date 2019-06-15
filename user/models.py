from django.db import models
from django.contrib.auth.models import AbstractUser
from . import globalvalues

# Create your models here.
class CustomUser(AbstractUser):
    birthyear = models.PositiveSmallIntegerField(
        choices=globalvalues.get_birthyear(), null=True)
    gender = models.PositiveSmallIntegerField(choices=globalvalues.get_gender()
                                              , null=True)
    race = models.PositiveSmallIntegerField(choices=globalvalues.get_race(),
                                            null=True)


