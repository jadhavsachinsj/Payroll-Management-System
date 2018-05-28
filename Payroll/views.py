from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
# import datetime
from datetime import datetime
import calendar


# import models

from .models import Salary
from employee.models import Employee
from Attendance.models import Attendance
from Company.models import Holiday, CompanyDeductions


# import Forms

from .forms import SalaryForm, EmployeeSelectForm


def salary(request):
    if request.method == 'POST':
        employee_select_form = EmployeeSelectForm(request.POST or None)

        if employee_select_form.is_valid():
            emp = employee_select_form.save(commit=False)
            print('Employee', emp.date)
            date = emp.date
            year = date.year
            month = date.month
            print('date:', year, month)

            return redirect('salary', pk=emp.employee.pk, month=month, year=year)
    else:
        employee_select_form = EmployeeSelectForm()

        return render(request, 'employee_select.html', {'employee_select_form': employee_select_form})


def employee_salary(request, pk, month, year):

    print('Request is :', request, '\t pk is :',
          pk, 'month:', type(month), 'year:', type(year))

    sat_in_month = calendar.SATURDAY
    sun_in_month = calendar.SUNDAY

    matrix = calendar.monthcalendar(int(year), int(month))
    saturday_count = sum(1 for x in matrix if x[sat_in_month] != 0)
    sunday_count = sum(1 for x in matrix if x[sun_in_month] != 0)

    total_sat_sun = sum([saturday_count, sunday_count])
    #    print('total_sat_sun', total_sat_sun)

    annual_salary = Employee.objects.filter(pk=pk).latest('pk').salary
    deductions = CompanyDeductions.objects.filter(
        company_id=request.user.employee.company).latest('id')
    #   print('deductons', deductions.basic)

    s_date = datetime.strptime(str(year)+str(month), '%Y%m')
    #  print("llllllllll", s_date)
    start_date = s_date.strftime('%Y-%m-%d')

    end_date = datetime.strptime(
        str(year)+str(month)+str(calendar.monthrange(s_date.year, s_date.month)[1]), '%Y%m%d')

    e_date = end_date.strftime('%Y-%m-%d')

    first_day = s_date.strftime("%d")

    last_day = end_date.strftime("%d")

    # print("First Day:", first_day, '\t last day', last_day)

    present_count = Attendance.objects.filter(
        employee_id=pk, date__range=[str(start_date), str(e_date)], mark='P').count()

    if present_count != 0:

        gross_salary = annual_salary/12
        print('monthly_salary', gross_salary)

        basic_salary = (deductions.basic/100) * float(gross_salary)
        print('basic_salary', basic_salary)

        hra = (deductions.hra/100) * basic_salary

        conveyance_allow = deductions.conveyance_allow

        professional_tax = deductions.professional_tax

        # salary_per_day = round(float(gross_salary)/float(last_day), 2)
        salary_per_day = round(float(basic_salary)/float(last_day), 2)
        print("Salary Per Day:", salary_per_day)

        present_count = Attendance.objects.filter(
            employee_id=pk, date__range=[str(start_date), str(e_date)], mark='P').count()

        seek_leave_count = Attendance.objects.filter(
            employee_id=pk, date__range=[str(start_date), str(e_date)], leave_type='C').count()
        privilege_leave_count = Attendance.objects.filter(
            employee_id=pk, date__range=[str(start_date), str(e_date)], leave_type='C').count()

        total_leaves = sum([seek_leave_count, privilege_leave_count])

        holiday_count = Holiday.objects.filter(company_id=request.user.employee.company, date__range=[
            str(start_date), str(e_date)]).count()

        special_allowence = float(
            gross_salary) - (sum([float(basic_salary), float(hra), float(conveyance_allow), float(professional_tax)]))

        employee_total = sum([present_count, total_sat_sun,
                              holiday_count, total_leaves])
        total_salary_count = (employee_total * salary_per_day)

        gross_earnings = sum(
            [float(hra), float(conveyance_allow), float(special_allowence), float(total_salary_count)])

        print('special_allowence', special_allowence)
        print('###### total salary ######', total_salary_count)
        print('gross_earnings', gross_earnings)

        print('employee_total', employee_total)

        print('holiday_count', holiday_count)

        print('Seek Leave', seek_leave_count)
        print('privilege Leave:', privilege_leave_count)

        print("Persent Count ", present_count)
        print('hra', hra)

        loss_pay = Attendance.objects.filter(
            employee_id=pk).latest('pk').loss_of_pay
        print('basic_salary', type(basic_salary))
        if request.method == 'GET':
            salary_form = SalaryForm(request.GET or None)
            obj, created = Salary.objects.get_or_create(employee_id=pk,
                                                        date=datetime.now(),
                                                        basic=basic_salary,
                                                        hra=hra,
                                                        conveyance_allow=conveyance_allow,
                                                        special_allowence=special_allowence,
                                                        professional_tax=professional_tax,
                                                        gross_earnings=gross_earnings,
                                                        total_days=present_count,
                                                        public_holidays=holiday_count)

            salary_form = SalaryForm(instance=obj)

            print("Errors IS:", salary_form.errors)

            # if salary_form.is_valid():
            #       print("Form is Valid")

            #salary = salary_form.save(commit=False)
            # salary.save()

            messages.success(request, 'salary is Generated  successfully..!')

            # return redirect('salary', pk=salary.employee.pk)
            return render(request, 'salary.html', {'salary_form': salary_form})
        # else:
        #     print('Form is not valid')
        #     messages.error(request, 'salary is Not Added')
        #     salary_form = SalaryForm()
        else:

            messages.error(request, 'salary is not added2')
            print('Request is Not Post')
            salary_form = SalaryForm()

    else:

        messages.error(
            request, 'Attendence Is Empty So salary is not Generated')
        salary_form = SalaryForm()

    return render(request, 'salary.html', {'salary_form': salary_form, })
