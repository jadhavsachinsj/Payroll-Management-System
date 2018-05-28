from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from .models import Employee, DesignationHistory
from django.views.generic import ListView
from .forms import AddEmployeeForm, UserForm, LoginForm, DesignationHistoryForm, JobTypeHistoryForm, DepartmentHistoryForm
from Company.models import Designation, WorkType, Department, JobType

# Import For Employee Registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
# Company Add
import Company
from Company.models import Company
from Company.forms import CompanyForm


# For Employee Profile
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# For Company Add

from .models import Company


def employee_register(request):

    print("sjhjdsh", request.user)
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST or None)
        company_add = CompanyForm(request.POST or None)
        employee_form = AddEmployeeForm(request.POST or None, request.FILES)
     #   print(form)
     #   print(employee_form)
     #   print(company_add)

        if company_add.is_valid() and form.is_valid() and employee_form.is_valid():

            try:
                print("zzzzzzzzzzzzzzzzzzzzzzzz", form)

                company = company_add.save()
                print("COMPANY IS----------------", company)
                print("************************************")

                user = form.save()
                print("USER IS", user)
                print("888888888888888888888888888888888888888888888888888")

                employee = employee_form.save(commit=False)
                employee.company = company
                employee.user = user

                employee = employee_form.save()
                # print(employee)
                messages.success(request, 'Registration successfull')
                # return redirect('employee_login')
                return render(request, 'signup_complete.html', {})
            except:
                print('Exception occures..! ')
        else:
            print("asdjksh")
            messages.error(request, 'Form is Not Valid')
            print("Error List ", form.errors)
            form = UserForm()
            company_add = CompanyForm()
            employee_form = AddEmployeeForm()
            context = {
                'company_add': company_add,
                'form': form,
                'employee_form': employee_form,
            }
            return render(request, 'Signup.html', context)

    else:
        print("request is Not Post")
        form = UserForm()
        company_add = CompanyForm()
        employee_form = AddEmployeeForm()
    context = {
        'company_add': company_add,
        'form': form,
        'employee_form': employee_form,
    }
    return render(request, 'Signup.html', context)


def employee_list(request):
    print(request.user.employee.company)
    queryset = Employee.objects.filter(company=request.user.employee.company)
    # queryset = User.objects.all()
    # employee = get_object_or_404(User, pk=request.user.employee.company.pk)
    print(queryset)

    # queryset = Employee.objects.all()

    context = {

        'object_list': queryset,
    }

    return render(request, 'base.html', context)  # context)


def employee_create(request):
    designation = Designation.objects.filter(
        company=request.user.employee.company)
    print("aaaaaaaaaaaa", request.method, designation)
    job_type = JobType.objects.filter(company=request.user.employee.company)

    department = Department.objects.filter(
        company=request.user.employee.company)
    if request.method == "POST":
        print(request.method)

        user_form = UserForm(request.POST or None)

        employee_form = AddEmployeeForm(
            request.POST, request.FILES)  # , instance=a)
        des_history_form = DesignationHistoryForm(request.POST)

        jobtype_history_form = JobTypeHistoryForm(request.POST)

        department_history_form = DepartmentHistoryForm(request.POST)

        print(employee_form, user_form)
        print("erfe", request.POST)

        if user_form.is_valid() and employee_form.is_valid() and des_history_form.is_valid() and jobtype_history_form.is_valid() and department_history_form.is_valid:

            try:

                user = user_form.save()
                employee = employee_form.save(commit=False)
                employee.user = user
                employee.company = request.user.employee.company
                print("sdsfsaaaaaaaaaaaaa", employee.company)
                employee.save()

                deshistory = des_history_form.save(commit=False)
                deshistory.employee = user.employee
                deshistory.company = request.user.employee.company
                deshistory = des_history_form.save()

                jobtype = jobtype_history_form.save(commit=False)
                jobtype.employee = user.employee
                jobtype.company = request.user.employee.company
                jobtype.date = datetime.datetime.now()
                jobtype.save()

                department_history = department_history_form.save(commit=False)
                department_history.employee = user.employee
                department_history.company = request.user.employee.company
                department_history.date = datetime.datetime.now()
                department_history.save()

                messages.success(request, 'Employee add successfull')

                return redirect('employee_list')

            except:

                print('Exception Occure..!')
        else:

            print("ERROR LIST IS:", employee_form.errors)
            messages.error(request, 'Form is Not Valid')

            employee_form = AddEmployeeForm()
            user_form = UserForm()
            des_history_form = DesignationHistoryForm()
            jobtype_history_form = JobTypeHistoryForm()
            department_history_form = DepartmentHistoryForm()

            return render(request, 'empEdit.html', {'user_form': user_form, 'employee_form': employee_form, 'des_history_form': des_history_form, 'jobtype_history_form': jobtype_history_form, 'department_history_form': DepartmentHistoryForm})
            print("SACHINJADHAV")

    else:

        employee_form = AddEmployeeForm()
        user_form = UserForm()
        des_history_form = DesignationHistoryForm()
        jobtype_history_form = JobTypeHistoryForm()
        department_history_form = DepartmentHistoryForm()
        context = {
            'user_form': user_form,
            'employee_form': employee_form,
            'des_history_form': des_history_form,
            'jobtype_history_form': jobtype_history_form,
            'department_history_form': DepartmentHistoryForm
        }

    return render(request, 'empEdit.html', context)


def employee_update(request, pk):

    print(request, pk)
    emp = get_object_or_404(Employee, pk=pk)
    # user = get_object_or_404(User, pk=employee.user.pk)
    print(emp, "user")
    if request.method == "POST":

        employee_form = AddEmployeeForm(request.POST or None,
                                        request.FILES, instance=emp)
        user_form = UserForm(request.POST or None, instance=emp.user)

        if employee_form.is_valid() and user_form.is_valid():
            try:

                user = user_form.save()
                emp = employee_form.save()
                # print("bvrtybn", emp, user)
                # emp.user = user
                # emp.save()
                # user.save()
                return redirect('employee_list')
            except:

                print('Exception Occures at employee_update Viev..!')

    else:

        user_form = UserForm(instance=emp.user)
        employee_form = AddEmployeeForm(instance=emp)

        context = {
            'user_form': user_form,
            'employee_form': employee_form,
        }

    return render(request, 'empEdit.html', context)


def employee_home(request):

    return render(request, 'index.html', {})


def employee_display(request, pk):
    print(request)

    user = get_object_or_404(User, pk=pk)
    print('1111111111111111', pk)
    print("askjdhjsahjh", user)

    context = {
        'user': user,
        #'employee': emp,
        #        'designation': designation,

    }
    print("AAAAAAA", context)

    return render(request, 'profile.html', context)
