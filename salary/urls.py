from django.conf.urls import url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    url(r'^salary/select/$', views.salary, name='select_salary'),

    url(r'^salary/add/$', views.salary_add, name='add_salary'),

    url(r'^salary/history/$', views.salary_history, name='salary_history'),

    url(r'^appraisal/history/$', views.appraisal_history, name='appraisal_history'),

    url(r'^salary/(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)/calculate/$',
        views.employee_salary, name='salary'),

    url(r'^salary/(?P<pk>\d+)/slip/$', views.export, name='salary_slip'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
