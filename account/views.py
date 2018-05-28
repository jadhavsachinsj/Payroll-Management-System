from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
# from django.http import HttpResponse

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from . forms import LoginForm
from django.contrib import messages

# 1st Function login


def home_view(request):
    print("Sachin", request)

    # return HttpResponse('HomePage!..')

    return render(request, 'Dashboard.html', {})


def login_view(request):

    print("Only Request", request.user)

    if request.method == "POST":

        print("Request.method:", request.method)
        form = LoginForm(request.POST or None)
        print(form)
        print(form.errors)

        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(request, username=username, password=password)
        print("REQUEST", request)
        # print(user.employee.company)

        if user is not None:
            # if user.is_superuser:

            #     login(request, user)

            #     return redirect('employee_list')
            # else:
            login(request, user)

            return redirect('employee_home')
        else:
            messages.error(request, 'invalid Employee', extra_tags='alert')

    else:
        print("aaaaaaaaaaaaaaaaaaa")
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)

    return render(request, 'Dashboard.html', {})
  # else:
    #

    # else:
    #     print("uuuuuuuuuuuuu")
    #     messages.error(request, 'invalid Employee')
    #     #
    #

    # if form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")

    #     return render(request,)
