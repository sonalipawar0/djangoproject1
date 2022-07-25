from django.contrib import admin
from car_app import models

# Register your models here.
from .models import Maker,Model_details,Car,Customer,Car_customer,Car_maker


class MyCarAdmin(admin.ModelAdmin):
    model = models.Car
    list_display = [
        
        "cid",
        "car_name",
        "desription",
        "model"
    ]

class MyCusomeradmin(admin.ModelAdmin):
    model = models.Customer
    list_display = [
        
        "cu_id",
        "cu_name",
        "address",
        "date" 
    ]



class Mymakeradmin(admin.ModelAdmin):
    model = models.Maker
    list_display = [
        
        "cm_id",
        "name"
        
    ]

class MyModel_detailsadmin(admin.ModelAdmin):
    model = models.Model_details
    list_display = [
        
        "mid",
        "model",
        "maker"
    ]

class MyCar_customeradmin(admin.ModelAdmin):
    model = models.Car_customer
    list_display = [
        
        "car_name",
        "cu_name"
    ]

class MyCar_makeradmin(admin.ModelAdmin):
    model = models.Car_maker
    list_display = [
        
        "car_name",
        "maker_name"
    ]


admin.site.register(models.Maker,Mymakeradmin)
admin.site.register(models.Model_details,MyModel_detailsadmin)
admin.site.register(models.Car_customer,MyCar_customeradmin)
admin.site.register(models.Customer,MyCusomeradmin)
admin.site.register(models.Car_maker,MyCar_makeradmin)
admin.site.register(models.Car,MyCarAdmin)










