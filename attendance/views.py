from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from datetime import date
import calendar
# Create your views here.

# For Attendence Model and View Imports
from django.contrib.auth.models import User
from .models import Attendance
from employee.models import DesignationHistory, JobTypeHistory, Employee
from company.models import Designation
from .forms import AttendanceForm, AttendanceHistory


def attendance_mark(request):
    todays_present = Attendance.objects.filter(
        date=datetime.now(), mark=1)
    present_count = Attendance.objects.filter(
        date=datetime.now(), mark=1).count()
    todays_absent = Attendance.objects.filter(date=date.today(), mark=0)
    absent_count = Attendance.objects.filter(date=date.today(), mark=0).count()

    if request.method == 'POST':

        attendance_form = AttendanceForm(request.POST or None)
        print(attendance_form.errors)

        if attendance_form.is_valid():
            try:

                attendance = attendance_form.save(commit=False)
                attendance.company = request.user.employee.company
                atten = Attendance.objects.filter(
                    employee_id=attendance.employee.id)
                jobtype = str(JobTypeHistory.objects.filter(
                    employee_id=attendance.employee_id,).latest('id').jobtype)

                if not atten:

                    if jobtype != 'Probation':

                        print("under IF Staement")

                        desig = DesignationHistory.objects.filter(
                            employee=attendance.employee).latest('id')
                        leave = Designation.objects.get(
                            id=desig.designation.id)
                        c_leave = leave.casual_leave
                        p_leave = leave.privilege_leave
                        attendance.rem_casual_leave = c_leave
                        attendance.rem_privilege_leave = p_leave

                        messages.success(
                            request, 'Ateendance Mark Successfuly..!')
                        attendance.save()
                    else:
                        desig = DesignationHistory.objects.filter(
                            employee=attendance.employee).latest('id')

                        leave = Designation.objects.get(
                            id=desig.designation.id)
                        c_leave = leave.casual_leave
                        p_leave = leave.privilege_leave
                        attendance.rem_casual_leave = c_leave
                        attendance.rem_privilege_leave = p_leave
                        attendance.save()
                else:

                    jobtype = str(JobTypeHistory.objects.filter(
                        employee_id=attendance.employee_id,).latest('id').jobtype)

                    attendance_exist = Attendance.objects.filter(
                        date=attendance.date, employee_id=attendance.employee_id).exists()
                    if attendance_exist != True:

                        if jobtype != 'Probation':
                            print("JOb Type IS Not PRobation")

                            p_leave = Attendance.objects.filter(
                                employee_id=attendance.employee.id).latest('id').rem_privilege_leave
                            c_leave = Attendance.objects.filter(
                                employee_id=attendance.employee.id).latest('id').rem_casual_leave
                            l_pay = Attendance.objects.filter(
                                employee_id=attendance.employee.id).latest('id').loss_of_pay
                            leave_type = attendance.leave_type
                            if attendance.mark == 0:
                                if attendance.leave_type == 'C':
                                    c_leave -= 1

                                    attendance.rem_casual_leave = c_leave
                                    attendance.rem_privilege_leave = p_leave
                                       
                                    messages.success(
                                        request, 'Privilege Leave Added Successfully..!')
                                elif leave_type == 'P':
                                    print('leave_type is P')
                                    p_leave -= 1

                                    attendance.rem_privilege_leave = p_leave
                                    attendance.rem_casual_leave = c_leave
                                    messages.success(
                                        request, 'Privilege Leave Added Successfully..!')

                                elif c_leave > 0:

                                    c_leave -= 1

                                    attendance.rem_casual_leave = c_leave
                                    attendance.rem_privilege_leave = p_leave
                                    messages.success(
                                        request, ' Leave Added in Casual Leave Successfully..!')

                                elif p_leave > 0:
                                    p_leave -= 1
                                    attendance.rem_privilege_leave = p_leave
                                    attendance.rem_casual_leave = c_leave
                                    messages.success(
                                        request, ' Leave Added in Privilege Leave Leave Successfully..!')

                                else:
                                    if c_leave == 0:
                                        l_pay += 1
                                        attendance.loss_of_pay = l_pay
                                        attendance.rem_casual_leave = c_leave
                                        attendance.rem_privilege_leave = p_leave
                                        messages.success(
                                            request, 'Leave Added in Loss of Pay Successfully..!')

                                    elif c_leave == 0:
                                        l_pay += 1
                                        attendance.loss_of_pay = l_pay
                                        attendance.rem_casual_leave = c_leave
                                        attendance.rem_privilege_leave = p_leave
                                        messages.success(
                                            request, 'Leave Added in Loss of Pay Successfully..!')

                            elif attendance.mark == 0.5:
                                attendance.rem_casual_leave = c_leave

                                attendance.rem_privilege_leave = p_leave
                                attendance.save()
                                messages.success(
                                    request, 'attendance mark Successfully..! for half day')

                            else:
                                attendance.rem_casual_leave = c_leave

                                attendance.rem_privilege_leave = p_leave
                                messages.success(
                                    request, 'attendance mark Successfully..!')

                            attendance.save()
                        else:  # this else for jobtype !=probation:
                            joined_date = User.objects.filter(
                                id=attendance.employee_id).values('date_joined')  # it returns Query sets so we have to convert it into date class
                            joined_date = joined_date[0]['date_joined']
                            after = (joined_date.month + 7) % 12 or 12
                            date1 = date.today()
                            s_date = datetime.strptime(
                                str(date1.year) + str(date1.month), '%Y%m')
                            start_date = s_date.strftime('%Y-%m-%d')

                            end_date = datetime.strptime(
                                str(date1.year)+str(date1.month)+str(calendar.monthrange(s_date.year, s_date.month)[1]), '%Y%m%d')

                            e_date = end_date.strftime('%Y-%m-%d')
                            if start_date <= str(attendance.date) <= e_date:

                                p_leave = Attendance.objects.filter(
                                    employee_id=attendance.employee.id).latest('id').rem_privilege_leave
                                c_leave = Attendance.objects.filter(
                                    employee_id=attendance.employee.id).latest('id').rem_casual_leave
                                l_pay = Attendance.objects.filter(
                                    employee_id=attendance.employee.id).latest('id').loss_of_pay

                                if attendance.mark == 0:
                                    count = Attendance.objects.filter(
                                        employee_id=attendance.employee.id, mark=0, date__range=(start_date, end_date)).count()
                                    if count <= 0:
                                        if attendance.leave_type == 'C':

                                            c_leave -= 1
                                            attendance.rem_casual_leave = c_leave
                                            attendance.rem_privilege_leave = p_leave
                                            attendance.save()
                                            messages.success(
                                                request, ' Leave Added in Casual Leave Successfully..! for Probation Employee')
                                        else:
                                            p_leave -= 1
                                            attendance.rem_privilege_leave = p_leave
                                            attendance.rem_casual_leave = c_leave
                                            attendance.save()
                                            messages.success(
                                                request, ' Leave Added in previlege  Leave Successfully..! for Probation Employee')

                                    else:
                                        l_pay += 1
                                        attendance.loss_of_pay = l_pay
                                        attendance.rem_privilege_leave = p_leave
                                        attendance.rem_casual_leave = c_leave

                                        messages.success(
                                            request, ' Leave Added in loss of pay Successfully..! for Probation Employee')
                                        attendance.save()
                                        attendance = Attendance.objects.filter(
                                            employee_id=attendance.employee.id, mark=0).count()
                                else:
                                    attendance.rem_privilege_leave = p_leave
                                    attendance.rem_casual_leave = c_leave
                                    attendance.save()
                                    messages.success(
                                        request, ' attendance mark Successfully..! for Probation Employee')


                    else:
                        messages.error(
                            request, 'Attendance is alrady exist...!')
            except Exception as e:
                messages.error(request, e)
                print('JJJJ')

        else:
            print('JJJJ')
            return redirect('add_attendance')
    else:
        attendance_form = AttendanceForm()
        return render(request, 'attendance.html', {'attendance': attendance_form, 'todays_present': todays_present, 'todays_absent': todays_absent, 'present_count': present_count, 'absent_count': absent_count})


def attendance_history(request):
    print(request.method)

    if request.method == 'POST':

        history_form = AttendanceHistory(request.POST or None)
        obj = history_form.save(commit=False)
        s_date = request.POST.get('from_date')
        e_date = request.POST.get('to_date')
        attendances = Attendance.objects.filter(
            employee_id=obj.employee_id, date__gte=s_date, date__lte=e_date)
        for o in attendances:
            name = o.employee

        return render(request, 'attendance_history.html', {'history': history_form, 'attendances': attendances, 'name': name})

    else:

        history_form = AttendanceHistory()
    return render(request, 'attendance_history.html', {'history': history_form})
