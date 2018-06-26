from django import forms
from .models import Attendance
from django.forms.fields import DateField


class DateInput(forms.DateInput):
    input_type = 'date'


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'employee',
            'date',
            'mark',
            'leave_type',
        ]
        widgets = {
            'employee': forms.Select(
                attrs={'class': 'form-control', }),
            'date': DateInput(attrs={'class': 'form-control'}),
            'mark': forms.Select(
                attrs={'class': 'form-control', }),
            'leave_type': forms.Select(
                attrs={'class': 'form-control', }),
            'rem_privilege_leave': forms.NumberInput(
                attrs={'class': 'form-control', }),
            'rem_casual_leave': forms.NumberInput(
                attrs={'class': 'form-control', }),
        }


class AttendanceHistory(forms.ModelForm):
    from_date = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control'}))
    to_date = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Attendance
        fields = ['employee',
                  'from_date',
                  'to_date',
                  ]

        widgets = {
            'employee': forms.Select(
                attrs={'class': 'form-control'}),
        }
