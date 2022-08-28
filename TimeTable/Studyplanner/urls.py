#importing the libraries

from django.urls import path
#importing views.py file
from . import views

#calling the function in views 
urlpatterns=[
    path('home',views.index),
    path('<day>',views.timetable)
]
