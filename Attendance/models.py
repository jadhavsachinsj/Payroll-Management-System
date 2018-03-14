from django.db import models
from django.utils import timezone
# Create your models here.
#from employee.models import Employee
import employee
from employee.models import Employee




class Attendance(models.Model):


    MARK_FOR_ATTENDANCE=(
        ('P', 'PRESENT'),
        ('A', 'ABSENT'),
        ('W', 'WORK FROM HOME'),
        ('H', 'HALF DAY'),
    )

    LEAVE_TYPE=(
        ('C', 'CASUAL LEAVE'),
        ('P', 'PRIVILEGE LEAVE'),
        ('S', 'SEEK LEAVE'),
    )
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    date= models.DateField(auto_now= False, auto_now_add= True)
    mark= models.CharField(max_length=15, blank=False, null= False, default= 'P', choices= MARK_FOR_ATTENDANCE)
    leave_type= models.CharField(max_length=16, blank=True, null= True, choices= LEAVE_TYPE)
    rem_privilege_leave= models.IntegerField(blank= True, null= True)
    rem_casual_leave= models.IntegerField(blank= True, null= True)
    #work_type             =models.


    # def publish(self):
    #     self.date=




    def __str__(self):
        return '{}'.format(self.date)
