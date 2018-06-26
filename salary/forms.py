from django import forms
from .models import Salary
from employee.models import Employee, EmployeeSalary
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
                attrs={'class': 'form-control', 'readonly': 'True'}),
            'date': DateInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),
            'basic': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),
            'hra': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),
            'conveyance_allow': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'special_allowence': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),
            'professional_tax': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'income_tax': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'loss_of_pay': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'gross_earnings': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'gross_deduction': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'total_days': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'weekly_off': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'public_holidays': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'paid_days': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),

            'net_salary': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'True'}),


        }

 

class EmployeeSelectForm(forms.ModelForm):
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
            'date': DateInput(attrs={'class': 'form-control', }
            ),
        }

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id', False)
        super().__init__(*args, **kwargs)
        if company_id:
            self.fields['employee'].queryset = Employee.objects.filter(company_id=company_id)


class SalaryHistoryForm(forms.ModelForm):
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


class SalaryAddForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = [
            'employee',
            'salary',
            'updation_date',
            'effective_from'
        ]
        widgets = {
            'employee': forms.Select(
                attrs={'class': 'form-control', }
            ),
            'salary': forms.NumberInput(
                attrs={'class': 'form-control', }
            ),
            'updation_date': DateInput(
                attrs={'class': 'form-control', }
            ),
            'effective_from': DateInput(
                attrs={'class': 'form-control', }
            ),
        }


class AppraisalForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = [
            'employee'
        ]
        widgets = {
            'employee': forms.Select(
                attrs={'class': 'form-control', }
            ),
        }
