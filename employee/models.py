from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

from decimal import Decimal
import company
import attendance
from company.models import JobType, Designation, Department, Company
from django.contrib.auth.models import User


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=12, null=True)
    contact = models.CharField(
        max_length=12, blank=False, null=False, default='0')
    birth_date = models.DateField()
    address = models.TextField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_photo = models.ImageField(
        upload_to='payroll', height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):

        return '{} {}'.format(self.user.first_name, self.user.last_name)
    
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee)
    salary = models.DecimalField(decimal_places=2,
                                 max_digits=10,
                                 default=Decimal('0.0000000000')
                                 )
    updation_date = models.DateField(default=timezone.now)
    effective_from = models.DateField()

    def __str__(self):
        return self.employee.user.first_name + str(self.updation_date) + str(self.effective_from)


class DesignationHistory(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}{}{}'.format(self.employee, self.date, self.designation)

    def add_history(self):
        self.date = timezone.now()
        self.save()


class DepartmentHistory(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}{}{}'.format(self.employee, self.date, self.department)


class JobTypeHistory(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}{}{}'.format(self.employee, self.jobtype, self.date)


class LeaveHistory(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey('self', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    peivilege_leave = models.CharField(max_length=50, blank=True, null=False)
    casual_leave = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):

        return '{}{}{}'.format(self.employee, self.attendence, self.date)
