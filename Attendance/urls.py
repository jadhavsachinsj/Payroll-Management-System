from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^attendance/add/$', views.attendance_mark, name="add_attendance"),
]
