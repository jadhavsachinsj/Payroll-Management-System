from django.conf.urls import url
from django.contrib import admin
#import user
from . import views
#import login.views
#import login.urls
#import attendance.urls

urlpatterns = [
    url(r'^company/(?P<pk>\d+)$', views.company_display, name="company_display"),
    # url(r'^company/add/$', views.company_add, name="company_add"),
    url(r'^company/(?P<pk>\d+)/update/$',
        views.company_update, name="company_update"),
    url(r'^job-type/add/$', views.jobtype_add, name="add_jobtype"),

    url(r'^worktype/add/$', views.worktype_add, name="add_worktype"),
    url(r'^holiday/add/$', views.holiday_add, name="add_holiday"),
    url(r'^designation/add/$',
        views.designation_add, name="designation_add"),
    url(r'^department/add/$', views.department_add, name="add_department"),
    url(r'^deduction/add/$', views.deduction_add, name="deduction"),

]
