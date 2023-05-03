from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    CHOICES = (
      ("ADMIN", "admin"),
      ("MANAGER", "manager"),
      ("EMPLOYEE", "employee"),
    )
    first_name = models.CharField(max_length = 20,null=False)
    last_name = models.CharField(max_length = 20,null=False)
    username = models.CharField(max_length = 20, null=False, unique=True)
    email = models.EmailField(max_length=30, unique = True, null=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
    role = models.CharField(
        max_length=20,
        choices=CHOICES,
        default="EMPLOYEE" 

    )
 
    def __str__(self):
        return "{}".format(self.email)
    