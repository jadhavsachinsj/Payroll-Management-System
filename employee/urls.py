from django.conf.urls import url
from django.contrib import admin
# import employee
from . import views
# for Image
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #    url(r'index/$', views.employee_home,
    #       name="employee_home"),

    url(r'^home/$', views.employee_home,
        name="employee_home"),

    url(r'^signup/$', views.employee_register,
        name="employee_register"),


    url(r'^profile/(?P<pk>\d+)$', views.employee_display,
        name="employee_display"),
    # url(r'^home/profile/(?P<pk>\d+)$', views.employee_display,
    #    name="employee_display"),


    # For Employee Register
    url(r'^employee/$', views.employee_list,
        name="employee_list"),                                     # For Employee List Display

    url(r'^employee/add$', views.employee_create,
        name="employee_create"),                                   # For Employee Create

    url(r'^employee/(?P<pk>\d+)/update/$',
        views.employee_update, name="employee_update"),            # for Employee Update

    # url(r'^detail/', employee.views.employee_detail),
    # url(r'^list/', employee.views.employee_list),
    # url(r'^home/', employee.views.employee_home),
    # url(r'^delete/', employee.views.employee_delete),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
