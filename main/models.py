from django.db import models
from django.core.validators import (MaxValueValidator,MinValueValidator,EmailValidator)

# Create your models here.


class Personal(models.Model):
    appid=models.CharField(max_length=8,unique=True)
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=10)
    email_id=models.CharField(max_length=100,validators=[EmailValidator,])
    def __str__(self):
        return str(self.name)


class Mark(models.Model):
    appid=models.ForeignKey(Personal,on_delete=models.CASCADE)
    m1=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    m2=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    m3=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    m4=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    m5=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    total=models.IntegerField()
    def __str__(self):
        return str(self.appid)



    

