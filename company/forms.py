from django import forms
from django.forms.fields import DateField
from .models import Company, Designation, JobType, WorkType, Holiday, Department, CompanyDeductions


class DateInput(forms.DateInput):
    input_type = 'date'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'address_line1',
            #'address_line2',
            'city',
            'State',
            'postal_code',
            'country',
            'fax',
            'website',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company Name', }
            ),
            'address_line1': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company Address', }
            ),
            #'address_line2': forms.TextInput(
            #   attrs={'class': 'form-control',
            #         'placeholder': 'Company address2', }
            # ),
            'city': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company City', }
            ),
            'State': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company state', }
            ),
            'postal_code': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Postal Code', }
            ),

            'country': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company country', }
            ),

            'fax': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company fax', }
            ),
            'website': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Company website', }
            ),

        }


class DesignationAddForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = [
            #'company',
            'designation',
            'privilege_leave',
            'casual_leave',

        ]
        widgets = {
            #'company': forms.Select
            'designation': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Designation',
                    'maxlength': '50'
                }
            ),
            'privilege_leave': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Previlege Leave',
                    'maxlength': '3'
                }
            ),
            'casual_leave': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Casual Leave',
                    'maxlength': '3'
                }
            ),

        }


class JobtypeAddForm(forms.ModelForm):
    class Meta:
        model = JobType
        fields = [
            #'company',
            'job_type',
        ]
        widgets = {

            'job_type': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add JobType', }
            ),
        }


class WorktypeAddForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = [
            'type',
        ]
        widgets = {
            'type': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'add Worktype ', }),
        }


class HolidayAddForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = [
            'date',
            'holiday_name',
        ]
        widgets = {
            'date': DateInput(
                attrs={'class': 'form-control'}),
            'holiday_name': forms.TextInput(
                attrs={'class': 'form-control'
                       }),

        }


class DepartmentAddForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'department',
        ]
        widgets = {
            'department': forms.TextInput(
                attrs={'class': 'form-control'
                       }),
        }


class DeductionForm(forms.ModelForm):
    class Meta:
        model = CompanyDeductions
        fields = [
            # 'company',
            'basic',
            'hra',
            'conveyance_allow',
            'professional_tax',

        ]

        widgets = {
            'company': forms.TextInput(
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
        }
