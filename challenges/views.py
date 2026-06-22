from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def Monthly_challenge_by_number(request, month):
  return HttpResponse(month)

def Monthly_challenge(request, month):
  challenge_text = None
  if month == "january":
    challenge_text = "This works!"
  elif month == "february":
    challenge_text = "Work for at least 20 mins every day"
  else:
    return HttpResponseNotFound("This month is not allowed")
  return HttpResponse(challenge_text)