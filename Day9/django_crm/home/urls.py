from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('booking/',views.booking),
    path('form/',views.form,name='form'),
    path('customers/',views.customer_list,name="customers"),
]

