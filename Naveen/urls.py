from Naveen.views import *

from django.urls import path

app_name='king'

urlpatterns=[
    path('Charan/',Charan,name='Charan'),
    path('chiru/',chiru,name='chiru'),

]