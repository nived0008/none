
from django.db import models



class MyModel(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    GENDER_CHOICES=[('Male', 'Male'), ('Female', 'Female')]
    gender=models.CharField(choices=GENDER_CHOICES, max_length=10)
    phone=models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    account=models.CharField(choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')],max_length=20,null=True)
    materials=models.TextField()

