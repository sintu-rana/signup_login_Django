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
    
class TODO(models.Model):
  status_choices = [
  ('Pending', 'PENDING'),
  ('Inprogress', 'INPROGRESS'),
  ('Submitted', 'SUBMITTED'),
  ]
  priority_choices = [
  ('1', '1️⃣'),
  ('2', '2️⃣'),
  ('3', '3️⃣'),
  ('4', '4️⃣'),
  ('5', '5️⃣'),
  ('6', '6️⃣'),
  ('7', '7️⃣'),
  ('8', '8️⃣'),
  ('9', '9️⃣'),
  ('10', '🔟'),
  ]
  task = models.TextField()
  status = models.CharField(max_length=20 , choices=status_choices)
  user  = models.ForeignKey(CustomUser  , on_delete= models.CASCADE,null=False)
  date = models.DateTimeField(auto_now_add=True)
  priority = models.CharField(max_length=2 , choices=priority_choices)

  def __str__(self):
    return str(self.id)

class Manager(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  employee = models.ForeignKey('Employee', on_delete=models.CASCADE)


class Employee(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)