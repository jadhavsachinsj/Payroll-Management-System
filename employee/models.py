from django.db import models
from django.utils import timezone


# Create your models here.


class employee(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    address=models.TextField(max_length=200)
    join_date=models.DateField()
    email=models.EmailField(max_length=254)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )

    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    status=models.BooleanField()
   # leave_left=models.IntegerField()
    designation=models.CharField(max_length=50)




    def __str__(self):
        #return self.first_name, self.last_name
        return '{} {}'.format(self.first_name, self.last_name)
    
        
