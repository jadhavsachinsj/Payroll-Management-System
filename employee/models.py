from django.conf import settings
from django.db import models
from django.utils import timezone
from decimal import Decimal
import Company,Attendance
from Company.models import JobType,Designation,Department





class Employee(models.Model):
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    contact= models.CharField(max_length=12, blank= False, null= False, default= '0')
    alter_contact_no= models.CharField(max_length= 12, blank= False, null=False, default= '0')
    birth_date= models.DateField()
    address= models.TextField(max_length=200)
    join_date=models.DateField()
    email= models.EmailField(max_length=254)
    gender= models.CharField(max_length=1, choices=GENDER_CHOICES)
    status= models.BooleanField()
    profile_photo= models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=100)
    #leave_left=models.IntegerField()
    #designation        =models.CharField(max_length=50)
    confirmation_period= models.IntegerField(default=0,blank=False)





    def __str__(self):
        #return self.first_name, self.last_name
        return '{} {}'.format(self.first_name, self.last_name)




class DesignationHistory(models.Model):


    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation= models.ForeignKey(Designation, on_delete=models.CASCADE)
    date= models.DateField(auto_now=True, auto_now_add=False)



    def __str__(self):
        return '{}{}{}'.format(self.Employee,self.date,self.designation)


class DepartmentHistory(models.Model):


    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    date= models.DateField(auto_now=False, auto_now_add=True)





    def __str__(self):
        return '{}{}{}'.format(self.Employee,self.date,self.department)




class JobTypeHistory(models.Model):


    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    jobtype= models.ForeignKey(JobType, on_delete= models.CASCADE)
    date= models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return '{}{}{}'.format(self.Employee, self.jobtype,self.date)



class LeaveHistory(models.Model):


    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance= models.ForeignKey('self', on_delete=models.CASCADE)
    date= models.DateField(auto_now=True,auto_now_add=False)
    peivilege_leave= models.CharField(max_length=50,blank=True,null=False)
    casual_leave= models.CharField(max_length=50,blank=True,null=False)



    def __str__(self):

        return '{}{}{}'.format(self.Employee,self.attendence,self.date)










# class Salary(models.Model):
#     user                  =models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
#     date                  =models.DateField()
#     basic                 =models.FloatField()
#     hra                   =models.FloatField( default = '0.0' )
#     conv_allowence        =models.FloatField( default = '0.0')
#     special_allowence     =models.FloatField( default = '0.0')
#     prof_tax              =models.DecimalField( max_digits = 20, decimal_places = 4, default = Decimal('0.0000'))
#     income_tax            = models.DecimalField( max_digits = 20, decimal_places = 4, default = Decimal('0.0000'))
#     loss_of_pay           =models.DecimalField( max_digits = 20, decimal_places = 4, default = Decimal('0.0000'))
#     gross_earnings        =models.DecimalField( max_digits = 20, decimal_places = 4, default = Decimal('0.0000'))
#     deductions            =models.DecimalField( max_digits = 20, decimal_places = 4, default = Decimal('0.0000'))
#     total_days            =models.IntegerField( default =0)
#     weekly_off            =models.IntegerField( default = 0)
#     public_holidays       =models.IntegerField(default = 0)
#     paid_days             =models.IntegerField( default = 0)
#     net_salary            =models.IntegerField(default=0)







#     def __str__(self):
#         return '{}  {}'.format(self.user, self.date)

# class Attendance(models.Model):
#     first_name   =models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     MARK=(
#         ('P','Present'),
#         ('a','absent'),
#         ('h','halfday'),
#     )

#     LEAVE_TYPE=(
#         ('n','enter'),
#         ('s','SeekLeave'),
#         ('c','CausualLeave'),

#     )


#     first_name               =models.ForeignKey(employee, default = False, blank = True)
#     date                     =models.DateField()
#     mark                     =models.CharField(max_length=7,choices=MARK,default=False)
#     leave_type               =models.CharField(max_length=3, choices=LEAVE_TYPE,null=True,default='n')
#     #work_from_home           =models.BooleanField()
#     prev_leave_left          =models.IntegerField(default=0)
#     casual_leave_left        =models.IntegerField(default=0)
#     #worke_type               =models.




#     def __str__(self):
#         return '{}{}'.format(self.first_name,self.date)

# class Company(models.Model):
#     name          =models.CharField(max_length=50,blank=False,null=False)
#     location      =models.TextField(max_length=200,blank=False,null=False)
#     #fax           =models.
#     website       =models.EmailField(max_length=100)



#     def __str__(self):
#         return self.name


# class Holiday(models.Model):
#     #user           =models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
#     #comany_id     =model.ForeignKey('Company')
#     date          =models.DateField()
#     holiday_name  =models.CharField(max_length=50,default='Sunday')


#     def __str__(self):
#         return self.date


# class Designation(models.Model):

#     DESIGNATION_IN_COMPANY=(
#         ("D",'Developer'),
#         ('T','Tester'),
#         ('H','HR'),
#         ('M','Manager')
#     )
#     designation         =models.CharField(max_length=10,blank=True, choices=DESIGNATION_IN_COMPANY , default='D')
#     prev_leave_allowed  =models.IntegerField(default=0,blank=False,null=False)
#     casual_leave_allowed=models.IntegerField(default=0,blank=False,null=False)
#     salary              =models.IntegerField(default=0,blank=False,null=False)





#     def __str__(self):
#         return designation
