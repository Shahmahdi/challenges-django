from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
  "january": "Eat no meat on January",
  "february": "Work for at least 20 mins every day",
  "march": "March challenges",
  "april": "Eat no meat on april",
  "may": "Eat no meat on may",
  "june": "Eat no meat on june",
  "july": "Eat no meat on july",
  "august": "Eat no meat on august",
  "september": "Eat no meat on september",
  "october": "Eat no meat on october",
  "november": "Eat no meat on november",
  "december": "Eat no meat on december",
}

def Monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("Invalid month")
  
  redirect_month = months[month - 1]
  return HttpResponseRedirect("/challenges/" + redirect_month)

def Monthly_challenge(request, month):
  # challenge_text = None
  # if month == "january":
  #   challenge_text = "This works!"
  # elif month == "february":
  #   challenge_text = "Work for at least 20 mins every day"
  # else:
  #   return HttpResponseNotFound("This month is not allowed")
  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound("This month is not allowed")