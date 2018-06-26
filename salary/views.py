from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
# import datetime
from datetime import datetime
from datetime import date
import calendar
from num2words import num2words


# import models

from .models import Salary
from employee.models import Employee, JobTypeHistory, DesignationHistory, DepartmentHistory, EmployeeSalary
from attendance.models import Attendance
from company.models import Holiday, CompanyDeductions


# import Forms

from .forms import SalaryForm, EmployeeSelectForm, SalaryHistoryForm, SalaryAddForm, AppraisalForm


# import for Import Export

from .resources import SalaryResource


# import for weasyprint

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML


def salary(request):
    company_id = request.user.employee.company
    if request.method == 'POST':
        employee_select_form = EmployeeSelectForm(request.POST or None)

        if employee_select_form.is_valid():
            emp = employee_select_form.save(commit=False)
            date = emp.date
            year = date.year
            month = date.month
            return redirect('salary', pk=emp.employee.pk, month=month, year=year)
    else:
        employee_select_form = EmployeeSelectForm(company_id=company_id)

        return render(request, 'employee_select.html', {'employee_select_form': employee_select_form})


def salary_add(request):

    if request.method == 'POST':
        add_salary_form = SalaryAddForm(request.POST or None)

        if add_salary_form.is_valid():
            add_salary = add_salary_form.save()
            messages.success(
                request, 'Salary Added for Employee {}...!'.format(add_salary.employee))
            return redirect('select_salary')
        else:
            messages.error(
                request, 'Salary Form is not valid plz check again ..!')
            add_salary_form = SalaryAddForm()
            return render(request, 'salary_add.html', {'add_salary': add_salary_form})
    else:
        add_salary_form = SalaryAddForm()
        return render(request, 'salary_add.html', {'add_salary': add_salary_form})


def salary_history(request):

    if request.method == 'POST':
        history_select_form = SalaryHistoryForm(request.POST or None)

        if history_select_form.is_valid():
            emp = history_select_form.save(commit=False)
            name = emp.employee.first_name + " " + emp.employee.last_name
            history = Salary.objects.filter(
                employee_id=emp.employee.id)
            return render(request, 'salary_history.html', {'form': history_select_form, 'history': history, 'name': name})
        else:
            messages.error(request, 'form is not valid plz try again...!')
            history_select_form = SalaryHistoryForm()
            return render(request, 'salary_history.html', {'form': history_select_form})

    else:
        history_select_form = SalaryHistoryForm()
        return render(request, 'salary_history.html', {'form': history_select_form})


def employee_salary(request, pk, month, year):

    print('Request is :', request, '\t pk is :',
          pk, 'month:', type(month), 'year:', type(year))

    sat_in_month = calendar.SATURDAY
    sun_in_month = calendar.SUNDAY

    matrix = calendar.monthcalendar(int(year), int(month))
    saturday_count = sum(1 for x in matrix if x[sat_in_month] != 0)
    sunday_count = sum(1 for x in matrix if x[sun_in_month] != 0)

    total_sat_sun = sum([saturday_count, sunday_count])

    annual_salary = EmployeeSalary.objects.filter(
        employee_id=pk, effective_from__lte=datetime.today().date()).latest('id').salary

    deductions = CompanyDeductions.objects.filter(
        company_id=request.user.employee.company).latest('id')

    s_date = datetime.strptime(str(year)+str(month), '%Y%m')
    start_date = s_date.strftime('%Y-%m-%d')

    end_date = datetime.strptime(
        str(year)+str(month)+str(calendar.monthrange(s_date.year, s_date.month)[1]), '%Y%m%d')

    e_date = end_date.strftime('%Y-%m-%d')

    first_day = s_date.strftime("%d")

    last_day = end_date.strftime("%d")

    present_count = Attendance.objects.filter(
        employee_id=pk, date__range=[str(start_date), str(e_date)], mark=1).count()
    absent_count = Attendance.objects.filter(employee_id=pk, date__range=[
        str(start_date), str(e_date)], mark=0).count()

    if present_count != 0:
        jobtype = JobTypeHistory.objects.filter(
            employee_id=pk).latest('id').jobtype
        gross_salary = annual_salary/12
        basic_salary = (deductions.basic/100) * float(gross_salary)
        hra = (deductions.hra/100) * basic_salary
        conveyance_allow = deductions.conveyance_allow
        professional_tax = deductions.professional_tax
        salary_per_day = round(float(basic_salary)/float(last_day), 2)
        present_count = Attendance.objects.filter(
            employee_id=pk, date__range=[str(start_date), str(e_date)], mark=1).count()
        seek_leave_count = Attendance.objects.filter(
            employee_id=pk, date__range=[str(start_date), str(e_date)], leave_type='C').count()
        privilege_leave_count = Attendance.objects.filter(
            employee_id=pk, date__range=[str(start_date), str(e_date)], leave_type='P').count()

        total_leaves = sum([seek_leave_count, privilege_leave_count])

        holiday_count = Holiday.objects.filter(company_id=request.user.employee.company, date__range=[
            str(start_date), str(e_date)]).count()

        special_allowence = float(
            gross_salary) - (sum([float(basic_salary), float(hra), float(conveyance_allow), float(professional_tax)]))

        employee_total = sum([present_count, total_sat_sun,
                              holiday_count, total_leaves])
        total_salary_count = (employee_total * salary_per_day)
        loss_pay = Attendance.objects.filter(
            employee_id=pk).latest('pk').loss_of_pay
        loss_pay_calculation = (loss_pay * salary_per_day)

        gross_earnings = sum([float(total_salary_count * (45/100)), float(hra), float(
            conveyance_allow), float(special_allowence), float(total_salary_count)])

        gross_deduction = sum([float(professional_tax), ])

        net_salary = gross_earnings - gross_deduction
        try:
            obj = Salary.objects.get(employee_id=pk)
        except Salary.DoesNotExist:
            obj = Salary(employee_id=pk,
                         date=date.today(),
                         basic=basic_salary,
                         hra=hra,
                         conveyance_allow=conveyance_allow,
                         special_allowence=special_allowence,
                         professional_tax=professional_tax,
                         gross_earnings=gross_earnings,
                         gross_deduction=gross_deduction,
                         total_days=employee_total,
                         public_holidays=holiday_count,
                         net_salary=net_salary,
                         loss_of_pay=loss_pay_calculation)
            obj.save()
        if request.method == 'POST':

            salary = Salary.objects.filter(employee_id=pk).latest('id')
            company = request.user.employee.company
            company_address = request.user.employee.company.address_line1
            designation = DesignationHistory.objects.filter(
                employee_id=pk).latest('date').designation
            department = DepartmentHistory.objects.filter(
                employee_id=pk).latest('date').department

            month_year = datetime.strftime(salary.date, '%m-%Y')
            sal_in_words = str(num2words(salary.net_salary))
            context = {
                'company': company,
                'company_address': company_address,
                'designation': designation,
                'department': department,
                'employee': salary.employee,
                'date': salary.date,
                'month_year': month_year,
                'basic': salary.basic,
                'hra': salary.hra,
                'conveyance_allow': salary.conveyance_allow,
                'special_allowence': salary.special_allowence,
                'professional_tax': salary.professional_tax,
                'income_tax': salary.income_tax,
                'loss_of_pay': salary.loss_of_pay,
                'gross_earnings': salary.gross_earnings,
                'gross_deduction': salary.gross_deduction,
                'total_days': salary.total_days,
                'weekly_off': salary.weekly_off,
                'public_holidays': salary.public_holidays,
                'weekends': total_sat_sun,
                'paid_days': salary.paid_days,
                'net_salary': salary.net_salary,
                'sal_in_words': sal_in_words,

            }

            html_string = render_to_string(
                'salaryslip.html', context)

            html = HTML(string=html_string)
            html.write_pdf(target='/tmp/salary_pdf.pdf')

            fs = FileSystemStorage('/tmp')

            with fs.open('salary_pdf.pdf') as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="salary_pdf.pdf"'
            messages.success(
                request, 'salary is Generated  successfully..!')

            return response

        else:
            salary_form = SalaryForm(request.GET or None)
            salary_form = SalaryForm(instance=obj)
            print(">>>>>>>>>>>")
            return render(request, 'salary.html', {'salary_form': salary_form, 'pk': pk})

    else:

        messages.error(
            request, 'Attendence Is Empty So salary is not Generated')
        salary_form = SalaryForm()
        return redirect('select_salary')


def export(request, pk):
    print(pk)
    salary = Salary.objects.filter(employee_id=1)

    paragraph = [salary]
    html_string = render_to_string(
        'salaryslip.html', {'paragraph': paragraph})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/salary_pdf.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('salary_pdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="salary_pdf.pdf"'
        return response

    return response

    # salary_resource = SalaryResource()
    # dataset = salary_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="salary.csv"'
    # return response
    # print(type(response))
    #    return render(request, 'salaryslip.html', {'response': response})


def appraisal_history(request):

    if request.method == 'POST':
        appraisal_history = AppraisalForm(request.POST or None)

        if appraisal_history.is_valid():
            name = ""
            try:
                appraisal_history_form = appraisal_history.save(commit=False)
                appraisal = EmployeeSalary.objects.filter(
                    employee_id=appraisal_history_form.employee.id)
                for a in appraisal:
                    name = a.employee
                    print(a.employee, a.salary,
                          a.updation_date, a.effective_from)

            except e as Exception:
                messages.error(request, e)
            return render(request, 'appraisal.html', {'form': appraisal_history, 'name': name, 'appraisal': appraisal})
        else:
            messages.error(
                request, 'Appraisal form is not valid plz check again...!')
            appraisal_history = AppraisalForm()
            return render(request, 'appraisal.html', {'form': appraisal_history})

    else:
        appraisal_history = AppraisalForm()
        return render(request, 'appraisal.html', {'form': appraisal_history})
