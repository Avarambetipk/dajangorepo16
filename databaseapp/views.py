from django.shortcuts import render
from  databaseapp.models import Employee
# Create your views here.
def retrieve_view(request):
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(esal__gte=29999.0)
    #emp_list = Employee.objects.filter(ename__endswith='th')
    #emp_list = Employee.objects.filter(esal__range=[900,10000])
    emp_list = Employee.objects.filter(ename__startswith='p')| Employee.objects.filter(esal__ite=999.0)
    return render(request,'databaseapp/index.html',{'emp_list':emp_list})
