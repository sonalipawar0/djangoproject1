from django.shortcuts import render
from .models import Maker,Model_details,Car,Customer,Car_customer,Car_maker



def all_data(request):
    data =Car.objects.all()
    return render(request, 'car_info.html',locals()) 
    
def model(request):
    m_data =Model_details.objects.all()
    return render(request, 'model_details.html',locals())

def car_maker(request):
    cm_data =Model_details.objects.all()
    return render(request, 'car_maker.html',locals())

def order(request):
    o_data =Car_customer.objects.all()
    return render(request, 'order.html',locals())
def maker(request):
    mk_data =Maker.objects.all()
    return render(request, 'maker.html',locals())

# Create your views here.
def dashborad(request):
    return render(request,'dashborad.html')