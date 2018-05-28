from django import forms
from .models import Salary
from employee.models import Employee
from django.forms.fields import DateField


class DateInput(forms.DateInput):
    input_type = 'date'


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = [
            'employee',
            'date',
            'basic',
            'hra',
            'conveyance_allow',
            'special_allowence',
            'professional_tax',
            'income_tax',
            'loss_of_pay',
            'gross_earnings',
            'gross_deduction',
            'total_days',
            'weekly_off',
            'public_holidays',
            'paid_days',
            'net_salary',
        ]
        widgets = {
            'employee': forms.TextInput(
                attrs={'class': 'form-control'}),
            'date': DateInput(
                attrs={'class': 'form-control'}),
            'basic': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'hra': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'conveyance_allow': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'special_allowence': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'professional_tax': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'income_tax': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'loss_of_pay': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'gross_earnings': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'gross_deduction': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'total_days': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'weekly_off': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'public_holidays': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'paid_days': forms.NumberInput(
                attrs={'class': 'form-control'}),

            'net_salary': forms.NumberInput(
                attrs={'class': 'form-control'}),


        }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['employee'].queryset = E


class EmployeeSelectForm(forms.ModelForm):
    #    date = forms.DateField()

    class Meta:
        model = Salary
        fields = [
            'employee',
            'date',

        ]
        widgets = {
            'employee': forms.Select(
                attrs={'class': 'form-control', }
            ),
            'date': DateInput(
                attrs={'class': 'form-control', }
            ),
        }
