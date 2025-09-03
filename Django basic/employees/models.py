from django.db import models

# Create your models here.
class Employess(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images")
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=100,blank=True)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)


    def __str__(self):
        return self.fname
