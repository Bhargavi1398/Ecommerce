from django.db import models

# Create your models here.
class Ecommerce(models.Model):
    name=models.CharField(max_length=20)
    category=models.CharField(max_length=100)
    about=models.TextField()
    image=models.CharField(max_length=100)
    #size = models.ForeignKey(size, on_delete=models.SET_NULL, null=True)
    price=models.IntegerField()
    discounted_price=models.IntegerField()

class Conformation(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    address=models.TextField()
    email=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    landmark=models.CharField(max_length=100)
