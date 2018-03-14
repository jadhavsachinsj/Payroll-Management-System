from django.conf.urls import url
from django.contrib import admin
import employee
from . import views


urlpatterns=[
    url(r'^create/',employee.views.employee_create),
    url(r'^detail/',employee.views.employee_detail),
    url(r'^list/',employee.views.employee_list),
    url(r'^home/',employee.views.employee_home),
    url(r'^delete/',employee.views.employee_delete),


]
