from django.contrib import admin
from .models import Employee,DesignationHistory,DepartmentHistory,JobTypeHistory,LeaveHistory#, Salary, Attendance, Company, Holiday, Designation
# Register your models here.

admin.site.register(Employee)
admin.site.register(DesignationHistory)
admin.site.register(DepartmentHistory)
admin.site.register(JobTypeHistory)
admin.site.register(LeaveHistory)
# admin.site.register(Designation)
