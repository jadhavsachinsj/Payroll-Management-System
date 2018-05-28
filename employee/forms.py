from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.forms.fields import DateField


from .models import Employee, Company, DesignationHistory, JobTypeHistory, DepartmentHistory
from Company.models import Designation, Department


# For Employee Registration
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(UserCreationForm):
    class Meta:

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'is_staff',
            'is_active',
            #'date_joined',
            'is_superuser',
        ]
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter User Name here ', ' maxlength': '255'}),

            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Name here', ' maxlength': '255'}),

            'middle_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Middle Name here', ' maxlength': '255'}),

            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Last Name here', ' maxlength': '255'}),

            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter An Email', ' maxlength': '100'}),

            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': ' Enter Password', ' maxlength': '100'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': ' Enter Password', ' maxlength': '100'}),


        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {


            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' Enter username', ' required': 'required', 'style': 'margin-bottom: 7px;'}),



            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': ' Enter Password', ' required': 'required', 'autofocus': 'autofocus', 'style': 'margin-bottom: 7px;'}),


        }


class AddEmployeeForm(forms.ModelForm):

    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )

    # select = forms.ChoiceField(widget=forms.Select, choices=GENDER_CHOICES)

    class Meta:

        model = Employee
        fields = [
            #'first_name',
            #'middle_name',
            #'last_name',
            #'user',
            'contact',
            #'alter_contact_no',
            'birth_date',
            'address',
            #'join_date',
            #'email',
            'gender',
            #'status',
            'profile_photo',
            'salary',
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Name here', ' maxlength': '255'}),

            'middle_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Middle Name here', ' maxlength': '255'}),

            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Last Name here', ' maxlength': '255'}),

            'contact': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Contact here', ' maxlength': '12'}),

            # 'alter_contact_no': forms.NumberInput(
            #    attrs={'class': 'form-control', 'placeholder': 'Enter Alternate Contact here', ' maxlength': '12'}),

            'birth_date': DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Birthdate'}),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Address here', ' maxlength': '255'}),

            #'join_date': DateInput(
            #   attrs={'class': 'form-control', 'placeholder': 'Select Date'}),

            #'status': forms.CheckboxInput(
            #    attrs={'class': 'custom-control custom-checkbox'}),

            'profile_photo': forms.ClearableFileInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Profile Photo'}),

            'salary': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Employee Salary here', ' maxlength': '10'}),


        }


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'confirm_password',
                  )
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', }),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', }),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'required': 'True'}),

        }


class DesignationHistoryForm(forms.ModelForm):
    class Meta:
        model = DesignationHistory

        fields = (
            'designation',

        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['designamtion'].queryset = Designation.objects.filter(
                request.user.employee.company)


class JobTypeHistoryForm(forms.ModelForm):
    class Meta:
        model = JobTypeHistory
        fields = ('jobtype',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['jobtype'].queryset = JobType.objects.filter(
                request.user.employee.company)


class DepartmentHistoryForm(forms.ModelForm):
    class Meta:
        model = DepartmentHistory
        fields = (
            'department',
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['department'].queryset = Department.objects.filter(
                request.user.employee.company)
