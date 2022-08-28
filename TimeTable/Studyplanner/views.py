#importing the libraries

from django.shortcuts import render
from django.http import HttpResponse

#creating function to display in the webpage

def index(request):
    return HttpResponse('Hey Bragadeesh, this is a timetable')

def timetable(request,day):
    if day=='monday':
        text='On Monday I will be learning Django'
    elif day=='tuesday':
        text='On tuesday I will be learning Big Data'
    elif day=='wednesday':
        text='On wednesday I will be learning Data Science'
    elif day=='thursday':
        text='On thursday I will be learning Dockers'
    elif day=='friday':
        text='On friday I will be learning Deep Learning'
    elif day=='saturday':
        text='On saturday I will be learning Artificial Intelligence'
    else:
        text='On sunday Its my free day'

    return HttpResponse(text)
