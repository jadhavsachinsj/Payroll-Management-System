from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

# For Attendence Model and View Imports

from .models import Attendance
from employee.models import DesignationHistory
from Company.models import Designation
from .forms import AttendanceForm


def attendance_mark(request):
    print("sachin", request)

    if request.method == 'POST':

        attendance_form = AttendanceForm(request.POST or None)
        print("dddddddddddddd", attendance_form)

        if attendance_form.is_valid():
            try:

                attendance = attendance_form.save(commit=False)
                print("atten", attendance.employee.id)
                attendance.company = request.user.employee.company
                print("attendence.company", attendance.company)

                atten = Attendance.objects.filter(
                    employee_id=attendance.employee.id)
                print("atten is Return :", atten)

                if not atten:
                    if attendance.mark != 'A':

                        print("under IF Staement")

                        desig = DesignationHistory.objects.filter(
                            employee=attendance.employee).latest('id')
                        print("designation", desig.designation)

                        leave = Designation.objects.get(
                            id=desig.designation.id)
                        c_leave = leave.casual_leave
                        p_leave = leave.privilege_leave
                        print('laeave is :', leave)
                        print('c_leave:', c_leave)
                        print('p_leave :', p_leave)
                        # if leave_type == 'A' and c_leave > 0:

                        #   c_leave -= 1
                        #  print("casual_leave is", c_leave)
                        attendance.rem_casual_leave = c_leave
                        attendance.rem_privilege_leave = p_leave

                        print("Casual_leave :", attendance.rem_casual_leave, '\n',
                              'Previllege_leave:', attendance.rem_privilege_leave)

                        print("ZZZZZZZZZZZZZZZZz", desig.designation.id)
                        messages.success(
                            request, 'Ateendance Mark Successfuly..!')
                        attendance.save()
                    else:
                        print("sachin")
                        messages.error(
                            request, 'Attendence Mark was Unsuccessfull...! Plz Select Correct Field')

                else:

                    p_leave = Attendance.objects.filter(
                        employee_id=attendance.employee.id).latest('id').rem_privilege_leave
                    c_leave = Attendance.objects.filter(
                        employee_id=attendance.employee.id).latest('id').rem_casual_leave
                    l_pay = Attendance.objects.filter(
                        employee_id=attendance.employee.id).latest('id').loss_of_pay
                    print('loss of pay is :', l_pay)
                    leave_type = attendance.leave_type
                    print("attendence form leave type", leave_type)

                    if attendance.mark == 'A':
                        if attendance.leave_type == 'C':
                            c_leave -= 1

                            attendance.rem_casual_leave = c_leave
                            attendance.rem_privilege_leave = p_leave
                            print('Casual leave after minus',
                                  attendance.rem_casual_leave)
                            messages.success(
                                request, 'Privilege Leave Added Successfully..!')
                            # attendance.save()
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

                                # elif attendance.mark == 'p':
                                #     attendance.rem_casual_leave = c_leave
                                #     attendance.rem_privilege_leave = p_leave
            except:
                print('Exception occure...!')
            attendance.save()

            return redirect('add_attendance')
        else:
            print("dassa", attendance_form.errors)
    else:
        print('Method Is Not Post')

        attendance_form = AttendanceForm()

        return render(request, 'attendance.html', {'attendance': attendance_form})
