from django.db import models
from django.utils import timezone
# Create your models here


class Company(models.Model):
    name             =models.CharField(max_length=50,blank=True,null=True)
    address_line1    =models.TextField(max_length=100,blank=True,null=True)
    address_line2    =models.TextField(max_length=100,blank=True,null=True)
    city             =models.CharField(max_length=50,blank=True,null=True)
    State            =models.CharField(max_length=50,blank=True,null=True)
    postal_code      =models.IntegerField()
    country          =models.CharField(max_length=50)
    fax              =models.TextField(max_length=50,blank=True,null=True)
    website          =models.CharField(max_length=50)




    def __str__(self):
        return self.name
    
    


class WorkType(models.Model):
    company     =models.ForeignKey(Company, on_delete=models.CASCADE)
    type        =models.CharField(max_length=50,blank=True,null=True)




    def __str__(self):
        return self.type



class Holiday(models.Model):
    company      =models.ForeignKey(Company, on_delete=models.CASCADE)
    date         =models.DateField(auto_now=False, auto_now_add=True)
    holiday_name =models.CharField(max_length=50,blank=True,null=True)





    def __str__(self):
        return self.holiday_name






class Designation(models.Model):
    company               =models.ForeignKey(Company, on_delete=models.CASCADE)
    designation           =models.CharField(max_length=50,blank=False,null=False)
    privilege_leave       =models.IntegerField(blank=True,null=True,default=0)
    casual_leave          =models.IntegerField(blank=True,null=True,default=0)
    




    def __str__(self):
        return self.designation






class Department(models.Model):
    company               =models.ForeignKey(Company, on_delete=models.CASCADE)
    department            =models.CharField(max_length=50, blank=False,null=False)



    def __str__(self):
        return self.department



class JobType(models.Model):
    company               =models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type              =models.CharField(max_length=50,blank=True,null=True)




    def __str__(self):
        return self.job_type




    
