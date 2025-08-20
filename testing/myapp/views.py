from django.shortcuts import render
from .models import Myapp

# Create your views here.
def home(request):
    data=Myapp.objects.all()
    return render(request,'index.html',{'data':data})