from django.conf import settings
from django.db import models
from django.utils import timezone
from decimal import Decimal
import Company
import Attendance
from Company.models import JobType, Designation, Department, Company
from django.contrib.auth.models import User


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.CharField(
        max_length=12, blank=False, null=False, default='0')
    birth_date = models.DateField()
    salary = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    address = models.TextField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_photo = models.ImageField(
        upload_to='payroll', height_field=None, width_field=None, max_length=100, null=True)

    #first_name = models.CharField(max_length=50)
    #middle_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)

    # alter_contact_no = models.CharField(
    #   max_length=12, blank=False, null=False, default='0')

    #join_date = models.DateField()
    #email = models.EmailField(max_length=254)

    #status = models.BooleanField()

    # leave_left=models.IntegerField()
    # designation        =models.CharField(max_length=50)
    #    confirmation_period = models.IntegerField(default=0, blank=False)
    def __str__(self):

        return '{} {}'.format(self.user.first_name, self.user.last_name)
        # return '{} {}'.format(self.address, self.profile_photo)


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
        return '{}{}{}'.format(self.Employee, self.date, self.department)


class JobTypeHistory(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}{}{}'.format(self.Employee, self.jobtype, self.date)


class LeaveHistory(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey('self', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    peivilege_leave = models.CharField(max_length=50, blank=True, null=False)
    casual_leave = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):

        return '{}{}{}'.format(self.Employee, self.attendence, self.date)
