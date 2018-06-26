# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Company, Holiday, Designation, JobType, WorkType, Department, CompanyDeductions
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm, DesignationAddForm, JobtypeAddForm, WorktypeAddForm, HolidayAddForm, DepartmentAddForm, DeductionForm
from django.contrib.auth.models import User
from django.contrib import messages

#@login_required


def company_display(request, pk):
    print(request.user.employee.company, pk)
    company = get_object_or_404(Company, pk=request.user.employee.company.pk)
    #user = request.user.employee.filter(name='amazatic')
    print("This is user Object", company)

    #queryset = Company.objects.all()
    context = {"company": company, }
    return render(request, 'company_list.html', context)


#@login_required
# def company_add(request):

#     if request.method == "POST":
#         form_company = CompanyForm(request.POST)
#         if form_company.is_valid():
#             form_company.save()
#             print("*"*20)
#             return redirect('company_display')
#             # return render(request, 'company_display', {'form': form_company})

#         else:
#             print("$"*30)
# #            return redirect('company_display')
#     else:
#         form_company = CompanyForm()
#     return render(request, "company.html", {'form': form_company})

def deduction_add(request):
    print("Request", request)
    deductions = CompanyDeductions.objects.all()
    print(deductions)

    if request.method == 'POST':

        deduction_form = DeductionForm(request.POST or None)

        if deduction_form.is_valid():

            deduction = deduction_form.save(commit=False)
            deduction.company = request.user.employee.company
            deduction.save()

            return redirect('deduction')
        else:
            messages.error(request, 'Form is not valid plz try again')
            deduction_form = DeductionForm()

    else:
        #        messages.error(request, 'Request is not Post')
        deduction_form = DeductionForm()

    return render(request, 'deduction_add.html', {'deduction_form': deduction_form, 'deductions': deductions})


def company_update(request, pk):
    print("aaaaaaaaaaa", request)
    company = get_object_or_404(Company, pk=pk)

#    print(type(company))
    if request.method == "POST":
        print("requset.method:", request.method)
        company_form1 = CompanyForm(request.POST or None, instance=company)

        if company_form1.is_valid():
            company = company_form1.save()
            return redirect('company_display')
        else:
            print("assssssssssssssssssssss")
            # return render(request, 'company.html', {'company_form': company_form1})
            return HttpResponse('status=201')

    else:
        print("ccccccccccccc")
        company_form1 = CompanyForm(instance=company)
       # print("sjhfjhsdjhfjhdsjhfjhdsj", company_form1)
        # context = {
        #   'company_form': company_form1,
        #}

    # {'company_form': company_form})
    return render(request, 'company.html', {'form': company_form1})


@login_required
def holiday_add(request):
    print('1', request)
    holiday_list = Holiday.objects.filter(
        company=request.user.employee.company)
    print(holiday_list)
    if request.method == "POST":
        form_holiday = HolidayAddForm(request.POST)
        if form_holiday.is_valid():
            holiday = form_holiday.save(commit=False)
            holiday.company = request.user.employee.company
            holiday = form_holiday.save()
            messages.success(request, 'Holiday added Sussessfully...')
            return redirect('add_holiday')
    else:
        print('222222222222')
 #       messages.error(
  #          request, 'Holiday is Not added Successfully..Pls Try Again..')
        form_holiday = HolidayAddForm()
    return render(request, "holiday_add.html", {'form': form_holiday, 'holiday_list': holiday_list})


def worktype_add(request):
    worktype_list = WorkType.objects.filter(
        company=request.user.employee.company)
    print('worktype_list :', worktype_list)

    if request.method == "POST":

        worktype_form = WorktypeAddForm(request.POST)

        if worktype_form.is_valid():

            worktype = worktype_form.save(commit=False)
            worktype.company = request.user.employee.company
            worktype = worktype_form.save()
            messages.success(request, 'WorkType Added Successfully...')
            return redirect('add_worktype')

    else:

        #messages.error(request, 'workType is Not Added...')
        worktype_form = WorktypeAddForm()
    return render(request, "add_worktype.html", {'form': worktype_form, 'worktype_list': worktype_list})


def designation_add(request):
    designation_list = Designation.objects.filter(
        company=request.user.employee.company)
    print(designation_list)

    if request.method == "POST":
        designationForm = DesignationAddForm(request.POST or None)
        print('ssssssssssssssssssss')

        if designationForm.is_valid():
            designation = designationForm.save(commit=False)
            designation.company = request.user.employee.company
            designation = designationForm.save()
            messages.success(request, 'Designation add Successfully ')
            context = {
                'designation': designation_list
            }
            # return rende(request, 'designation.html', context)
            return redirect('designation_add')
        else:
            print("form is not valid")
            messages.error(request, 'form is not valid')
    else:
        print('afjasejfksdjk')
#        messages.error(request, 'Method is not Post')
        designationForm = DesignationAddForm()
        return render(request, "designation.html", {'form': designationForm, 'designation': designation_list})


def department_add(request):
    print('Department')
    department_list = Department.objects.filter(
        company=request.user.employee.company)
    print(department_list)

    if request.method == "POST":

        form_department = DepartmentAddForm(request.POST)
        if form_department.is_valid():

            department = form_department.save(commit=False)
            department.company = request.user.employee.company
            department = form_department.save()
            messages.success(request, 'Department Added Successfully...')
            return redirect('add_department')
    else:
       #     messages.error(request, 'Department Is not Added Successfully...')
        form_department = DepartmentAddForm()
    return render(request, "department_add.html", {'form': form_department, 'department_list': department_list})


def jobtype_add(request):

    print(request)
    jobtype_list = JobType.objects.filter(
        company=request.user.employee.company)

    if request.method == "POST":

        print(request.method)
        form_job_type = JobtypeAddForm(request.POST)

        if form_job_type.is_valid():

            jobtype = form_job_type.save(commit=False)
            jobtype.company = request.user.employee.company
            jobtype = form_job_type.save()

            messages.success(request, 'Job Type Added Successfully...')

            return redirect('add_jobtype')
            # form_job_type = JobtypeAddForm()
            # context = {
            #     'jobtype_list': jobtype_list,
            #     'form': form_job_type
            # }
            # return render(request, 'jobtype_add.html', context)
        else:
            print('Jobtype form is not valid')

            form_job_type = JobtypeAddForm()
            messages.error(request, 'Form Is Not Valid...')
            return render(request, 'jobtype_add.html', {'form': form_job_type})

    else:

        print('aaaaaaaaaaaaa')
        form_job_type = JobtypeAddForm()

        return render(request, 'jobtype_add.html', {'form': form_job_type, 'jobtype_list': jobtype_list})
