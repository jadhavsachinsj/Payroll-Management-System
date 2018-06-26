from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from .models import Employee, DesignationHistory
from django.views.generic import ListView
from .forms import AddEmployeeForm, UserForm, LoginForm, DesignationHistoryForm, JobTypeHistoryForm, DepartmentHistoryForm
from company.models import Designation, WorkType, Department, JobType

# Import For Employee Registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
# Company Add
import company
from company.models import Company
from company.forms import CompanyForm


# For Employee Profile
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from salary.models import Salary

# For Company Add

from .models import Company, DepartmentHistory

# import for Email
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template import loader
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# import for chart
from django.db.models import Count, Q

from django.contrib.auth.decorators import login_required


def employee_register(request):

    print("sjhjdsh", request.user)
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST or None)
        company_add = CompanyForm(request.POST or None)
        employee_form = AddEmployeeForm(request.POST or None, request.FILES)

        if company_add.is_valid() and form.is_valid() and employee_form.is_valid():

            try:
                

                company = company_add.save()
                user = form.save()
                employee = employee_form.save(commit=False)
                employee.company = company
                employee.user = user
                employee = employee_form.save()
                messages.success(request, 'Registration successfull')
                return render(request, 'signup_complete.html', {})
            except:
                print('Exception occures..! ')
        else:
            messages.error(request, 'Form is Not Valid')
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
    print(request.user)
    print(request.user.employee.company)
    queryset = Employee.objects.filter(company=request.user.employee.company)
    context = {

        'object_list': queryset,
    }
    return render(request, 'base.html', context)  # context)


@login_required
def employee_create(request):

    designation = Designation.objects.filter(
        company=request.user.employee.company)
    job_type = JobType.objects.filter(company=request.user.employee.company)
    department = Department.objects.filter(
        company=request.user.employee.company)

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password1')
        company = request.user.employee.company
        user_form = UserForm(request.POST or None)
        employee_form = AddEmployeeForm(
            request.POST, request.FILES)
        des_history_form = DesignationHistoryForm(request.POST)

        jobtype_history_form = JobTypeHistoryForm(request.POST)

        department_history_form = DepartmentHistoryForm(request.POST)

        print(employee_form.errors, user_form.errors)

        if user_form.is_valid() and employee_form.is_valid() and des_history_form.is_valid() and jobtype_history_form.is_valid() and department_history_form.is_valid:

            try:

                user = user_form.save()
                employee = employee_form.save(commit=False)
                employee.user = user
                employee.company = request.user.employee.company

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

                email = user.email
                html_message = loader.render_to_string(
                    'employee_reg_msg.html',
                    {
                        'username': username,
                        'password': password,
                        'subject': 'Thank u for joining in ' + str(company),
                    }
                )

                send_mail('amazatic solutions', 'Congratulations', [
                          email], settings.EMAIL_HOST_USER, fail_silently=False, html_message=html_message)
                messages.success(request, 'Employee add successfull')
                return redirect('employee_list')

            except Exception as e:

                print('Exception Occure..!', e)
        else:
            messages.error(request, 'Form is Not Valid plz ')
            employee_form = AddEmployeeForm()
            user_form = UserForm()
            des_history_form = DesignationHistoryForm()
            jobtype_history_form = JobTypeHistoryForm()
            department_history_form = DepartmentHistoryForm()

            return render(request, 'empEdit.html', {'user_form': user_form, 'employee_form': employee_form, 'des_history_form': des_history_form, 'jobtype_history_form': jobtype_history_form, 'department_history_form': DepartmentHistoryForm})

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

    designation = Designation.objects.filter(
        company=request.user.employee.company)

    job_type = JobType.objects.filter(company=request.user.employee.company)

    department = Department.objects.filter(
        company=request.user.employee.company)

    if request.method == "POST":

        employee_form = AddEmployeeForm(request.POST or None,
                                        request.FILES, instance=emp)
        user_form = UserForm(request.POST or None, instance=emp.user)
        des_history_form = DesignationHistoryForm(request.POST)

        jobtype_history_form = JobTypeHistoryForm(request.POST)

        department_history_form = DepartmentHistoryForm(request.POST)

        if employee_form.is_valid() and user_form.is_valid() and des_history_form.is_valid() and jobtype_history_form.is_valid() and department_history_form.is_valid():
            try:

                user = user_form.save()
                emp = employee_form.save()

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
                return redirect('employee_list')
            except:

                print('Exception Occures at employee_update Viev..!')

    else:

        user_form = UserForm(instance=emp.user)
        employee_form = AddEmployeeForm(instance=emp)
        des_history_form = DesignationHistoryForm()

        jobtype_history_form = JobTypeHistoryForm()

        department_history_form = DepartmentHistoryForm()

        context = {
            'user_form': user_form,
            'employee_form': employee_form,
            'des_history_form': des_history_form,
            'jobtype_history_form': jobtype_history_form,
            'department_history_form': department_history_form,
        }

    return render(request, 'empEdit.html', context)


def employee_home(request):
    m_count = Employee.objects.filter(
        gender='M', company_id=request.user.employee.company).count()
    f_count = Employee.objects.filter(
        gender='F', company_id=request.user.employee.company).count()
    if request.user.is_superuser:
        return render(request, 'admin.html', {'m_count': m_count, 'f_count': f_count})
    else:
        return render(request, 'user.html', {})


def employee_display(request, pk):

    user = get_object_or_404(User, pk=pk)
    designation = DesignationHistory.objects.filter(
        employee_id=pk).latest('date')
    salary = Salary.objects.filter(employee_id=pk)
    for obj in salary:
        print("salary", obj.basic)

    department = DepartmentHistory.objects.filter(employee_id=pk).latest('pk')
    join_date = user.date_joined.strftime("%d-%B-%Y")
    context = {
        'user1': user,
        'designation': designation,
        'department': department,
        'date': join_date,
        'salary': salary,
    }

    return render(request, 'profile.html', context)
