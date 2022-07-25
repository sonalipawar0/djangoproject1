from django.db import models

# Create your models here.

# Create your models here.

class Maker(models.Model):
    cm_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Model_details(models.Model):
    mid=models.IntegerField(primary_key=True)
    model_name=models.CharField(max_length=255)
    maker = models.ForeignKey(Maker,on_delete=models.CASCADE)
    def __str__(self):
        return self.model_name

class Car(models.Model):
    cid=models.IntegerField(primary_key=True)
    car_name = models.CharField(max_length=255)
    desription = models.CharField(max_length=255)
    price=models.CharField( max_length=50)
    model = models.ForeignKey(Model_details,on_delete=models.CASCADE)
    def __str__(self):
        return self.car_name



class Customer(models.Model):
    cu_id=models.IntegerField(primary_key=True)
    cu_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)   
    date=models.DateField() 
    def __str__(self):
        return self.cu_name

class Car_customer(models.Model):

    car_name= models.ForeignKey(Car,on_delete=models.CASCADE)
    cu_name= models.ForeignKey(Customer,on_delete=models.CASCADE)


class Car_maker(models.Model):
    maker_name = models.ForeignKey(Maker,on_delete=models.CASCADE)
    car_name = models.ForeignKey(Car,on_delete=models.CASCADE)