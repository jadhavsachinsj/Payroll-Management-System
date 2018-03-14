from django.shortcuts import render #,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Employee
#from .forms import PostForm

def employee_create(request):
    return HttpResponse("<h1> well-come Sachin_create...!</h1>")


def employee_detail(request):
    return HttpResponse("<h1> well-come Sachin_detail...!</h1>")


def employee_list(request):
    queryset=employee.objects.all()
    context={
        "object_list":queryset,

    }


    # if request.user.is_authenticated():


    #     context={
    #         "first_name":"Sachin",
    #     }
    # else:
    #     context={
    #         "last_name":"Jadhav",

    #     }
    return render(request,"index.html",context)


def employee_home(request):
    return HttpResponse("<h1> well-come Sachin_home...!</h1>")

def employee_delete(request):
    return HttpResponse("<h1> well-come Sachin...!</h1>")
