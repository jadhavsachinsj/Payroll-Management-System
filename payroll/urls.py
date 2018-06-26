"""payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from0 my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import employee
from employee import views
import company
from company import views
# from rest_framework import routers, serilizers, viewsets     #This import is for Rest Framework


# class UserSerializer(serializers.HyprlinkdModelSerializer):
#     class Meat:
#         model = employee
#         fields = ('url', 'first_name', 'email', 'last_name')


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = employee.objects.all()
#     serializer_class = UserSerializer


# router = routers.DefaultRouter()
#router.Register(r'employee', UserViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include("account.urls")),
    url(r'', include("employee.urls")),
    url(r'', include("company.urls")),
    url(r'', include("attendance.urls")),
    url(r'', include("salary.urls")),
    #url(r'^api-auth/', include('rest_framework.urls')),

]
