from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app.models import Departments,Employees
# from app.serializers import DepartmentSerializer,EmployeeSerializer
# from django.core.files.storage import default_storage

# Create your views here.

def home(request):
    
    return render(request, "index.html", {'name':'Devskill'})