from django.db import models
from django.conf import settings
from decimal import Decimal


from django.contrib.auth.models import User

# Create your models here.


class Salary(models.Model):

    """
        This Model is Calculate Salary Of Employee
    """

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    basic = models.FloatField(default='0.0')
    hra = models.FloatField(default='0.0')
    conveyance_allow = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    special_allowence = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    professional_tax = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    income_tax = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    loss_of_pay = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    gross_earnings = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    gross_deduction = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))
    total_days = models.IntegerField(default=0)
    weekly_off = models.IntegerField(default=0)
    public_holidays = models.IntegerField(default=0)
    paid_days = models.IntegerField(default=0)
    net_salary = models.DecimalField(
        max_digits=10, decimal_places=4, default=Decimal('0.0000'))

    def __str__(self):
        return '{} {} {}'.format(self.employee.user.first_name, self.date, self.net_salary)
