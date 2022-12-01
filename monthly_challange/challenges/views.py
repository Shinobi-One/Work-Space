from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string

# Create your views here.

monthly_challenge = {
"january": "do not eat meat for entire month!",
"february": "walk 2 miles through out a day !",
"march":"go to the gym 3 times per a week! ",
"april":"THERE is no better time than now to start !",
"may": "no cheat meal is allowed",
"june": "now , run 2 mile a day !!",
"july": "100 push ups daily",
"August":"100 sit ups daily!!!",
"september": "no chicken is allowed",
"october": "drink 2 litre of water daily",
"november": None,
"december": "30 squats for fatality :))))",}



def index(request):
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html", {
        "month": months
    })
    


def numeric_month(request, month):
    response_number = list(monthly_challenge.keys())

    if month > len(response_number):
        return HttpResponseNotFound("please enter a valid month number")

    month_redirect = response_number[month -1]
    redirect_path = reverse("monthly_challenge", args=[month_redirect])
    return HttpResponseRedirect(redirect_path)


def month1(request, month):
    try:
        response_text = monthly_challenge[month]
        month_cap = month.capitalize()
        return render(request , "challenges/challenge.html", {
                      "text": response_text,
                      "month_list": month
                      })
    except KeyError  :
        response = render_to_string("404.html")
        return HttpResponseNotFound(response)

