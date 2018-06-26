from django.conf.urls import url
from django.contrib import admin
from . import views
# for Image 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     url(r'^home/$', views.employee_home,
        name="employee_home"),

    url(r'^signup/$', views.employee_register,
        name="employee_register"),


    url(r'^profile/(?P<pk>\d+)$', views.employee_display,
        name="employee_display"),

    url(r'^employee/$', views.employee_list,
        name="employee_list"),                                   

    url(r'^employee/add$', views.employee_create,
        name="employee_create"),                                   

    url(r'^employee/(?P<pk>\d+)/update/$',
        views.employee_update, name="employee_update"),            
        
        

 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
