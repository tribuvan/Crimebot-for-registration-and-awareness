from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import complaint,location,witness
from .forms import complaintform,witnessform
import requests
import json

def login_view(request,*args,**kwargs):
    return render(request,'login.html',{})




def home_view(request,*args,**kwargs):
    return render(request,'index.html',{})


def complaint_view(request):
    form = complaintform(request.POST or None)
    if form.is_valid():
        form.save()
        form = complaintform()
    context={
        'form': form 
    }
    return render(request, "register.html", context)


def witness_view(request):
    form = witnessform(request.POST or None)
    if form.is_valid():
        form.save()
        form = witnessform()
    context={
        'form': form 
    }
    return render(request, "witness.html", context)



def location_save(request):
    ip = requests.get("https://api.ipify.org?format=json")
    ip_data=json.loads(ip.text)
    res=requests.get("http://ip-api.com/json/"+ ip_data['ip'])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    user=location(latitude=location_data['lat'],longitude=location_data['lon'])
    user.save()
    return render(request,'location.html',{'data': location_data})
