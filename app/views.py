from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def siri(request):
    return HttpResponse('srujana and siri best friends')
