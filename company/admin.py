from django.contrib import admin
from .models import Company, WorkType, Holiday, Designation, Department, JobType, CompanyDeductions
# Register your models here.


admin.site.register(Company)
admin.site.register(WorkType)
admin.site.register(Holiday)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(JobType)
admin.site.register(CompanyDeductions)
