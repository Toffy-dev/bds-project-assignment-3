# views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from main.models import Employee
# Create your views here.


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


def index(request):
    employees = Employee.objects.all()
    return render(request, "employee/show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/emplist")
    return render(request, 'employee/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/emplist")
