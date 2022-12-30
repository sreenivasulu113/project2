from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def san(request):
    return HttpResponse('this my first name')
