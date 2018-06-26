from django.db import models
from django.utils import timezone
import employee
from employee.models import Employee
from company.models import Company
from datetime import date
from django.utils.timezone import now


class Attendance(models.Model):

    MARK_FOR_ATTENDANCE = (
        (1, 'PRESENT'),
        (0, 'ABSENT'),
        (0.5, 'HALF DAY'),
    )

    LEAVE_TYPE = (
        ('C', 'CASUAL LEAVE'),
        ('P', 'PRIVILEGE LEAVE'),
        ('S', 'SEEK LEAVE'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    mark = models.FloatField(
        blank=False, null=False, default=1, choices=MARK_FOR_ATTENDANCE)
    leave_type = models.CharField(
        max_length=16, blank=True, null=True, choices=LEAVE_TYPE)
    rem_privilege_leave = models.IntegerField(blank=True, null=True)
    rem_casual_leave = models.IntegerField(blank=True, null=True)
    loss_of_pay = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.employee.user.first_name)


class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_from = models.DateField()
    leave_to = models.DateField()
    leave_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{},{},'.format(self.employee.first_name, self.leave_type)
