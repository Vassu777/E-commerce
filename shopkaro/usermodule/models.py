from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField(max_length=100)


    def __str__(self) -> str:
        return self.name

