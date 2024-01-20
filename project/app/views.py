from django.shortcuts import render
#from django.http import HttpResponse
from .models import *


def home(request):
    return render(request,"home.html")

def insert(request):
    Fname=request.POST.get('fname')
    Lname=request.POST.get('lname')
    print(Fname)
    print(Lname)

    User.objects.create(Firstname=Fname,Lastname=Lname)
    return render(request,"home.html")

# Create your views here.