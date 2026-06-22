from django.shortcuts import render
from django.http import HttpResponse

def January(request):
  return HttpResponse("This works!")

def February(request):
  return HttpResponse("Work for at least 20 mins every day")