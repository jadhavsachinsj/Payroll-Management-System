from django.conf.urls import url

from django.contrib import admin
from django.conf import settings


from . import views


urlpatterns = [
    url(r'^salary/select/$', views.salary, name='select_salary'),
    url(r'^salary/(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)/calculate/$',
        views.employee_salary, name='salary'),
]
