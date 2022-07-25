from django.urls import path
from django.contrib import admin
from .import views
urlpatterns=[
path('',views.dashborad,name='dashborad'),
path('admin/', admin.site.urls),
path('car_info/',views.all_data,name="car_info"),
path('model/',views.model,name="model"),
path('order/',views.order,name="order"),
path('maker/',views.maker,name="maker"),
path('car_maker/',views.car_maker,name="car_maker"),

]