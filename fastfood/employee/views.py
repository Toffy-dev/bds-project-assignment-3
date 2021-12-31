# views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from main.models import Employee
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emplist')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/emplist.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    employees = Employee.objects.all()
    return render(request, "employee/show.html", {'employees': employees})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', {'employee': employee})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/emplist")
    return render(request, 'employee/edit.html', {'employee': employee})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/emplist")

