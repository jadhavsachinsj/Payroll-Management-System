from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^attendance/add/$', views.attendance_mark, name="add_attendance"),
    url(r'^attendance/history_by_name/$',
        views.attendance_history, name="history"),
]
