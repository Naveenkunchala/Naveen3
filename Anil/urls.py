from Anil.views import *


from django.urls import path


app_name='somthing'

urlpatterns=[
    path('Royal/',RoyalEnfield,name='RoyalEnfield'),
    path('Himalayan/',Himalayan,name='Himalayan'),
]