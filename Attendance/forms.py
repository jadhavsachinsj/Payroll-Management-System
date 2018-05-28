from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'employee',
            #'date',
            'mark',
            'leave_type',
            #            'rem_privilege_leave',
            #           'rem_casual_leave',
        ]
        widgets = {
            'employee': forms.Select(
                attrs={'class': 'form-control', }),
            'mark': forms.Select(
                attrs={'class': 'form-control', }),
            'leave_type': forms.Select(
                attrs={'class': 'form-control', }),
            'rem_privilege_leave': forms.NumberInput(
                attrs={'class': 'form-control', }),
            'rem_casual_leave': forms.NumberInput(
                attrs={'class': 'form-control', }),
        }

    # def save(self, *args, **kwargs):

    #     data = Attendance(**self.cleaned_data)

    #     print("DSAS", self.cleaned_data, data)
    #     return data
