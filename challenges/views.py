from django.http import response
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Walk for 10 minutes everyday",
    "march": "Learn django everyday",
    "april": "Learn react everyday",
    "may": "Learn python everyday",
    "june": "Learn node everyday",
    "july": "Learn ml everyday",
    "august": "Learn AI everyday",
    "september": "Learn c# everyday",
    "october": "Learn c++ everyday",
    "november": "Learn java everyday",
    "december": None,
}

# when clicking on month


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


# when string is entered in url


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        raise Http404()


# when integer is entered in url
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    rediret_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_month)
