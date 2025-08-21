from django.shortcuts import render
from .models import AboutUs
# Create your views here.

def aboutus(request):
    data=AboutUs.objects.all()
    about_data = {
        'about_data':data
    }
    return render (request,'aboutus.html',about_data)
