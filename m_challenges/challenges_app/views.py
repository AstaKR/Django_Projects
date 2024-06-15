from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
challenges = {

    "januvary":"Take an online course",
    "february":"Read every day",
    "march":"Write every day",
    "april":"Drawing or painting challenge",
    "may":"Photography challenge",
    "june":"Learn a new language",
    "jully":"Kindness challenge",
    "augest":"Journaling challenge",
    "september":"Daily affirmations",
    "october":"Sign up for a continuing education class",
    "november":"Eat fruits/veggies every day",
    "december":None
    }

def index(request):
    months = list(challenges.keys())
    return render(request, 'challenges_app/index.html', {"months": months})
    #
    # list_data = ""
    #
    # for month in challenges:
    #     capitalize_month = month.capitalize()
    #     reverse_month = reverse("monthly-challenge", args=[month])
    #     list_data  += f"<li><a href=\"{reverse_month}\">{capitalize_month}</a></li>"
    #
    # response_data = f"<ul>{list_data}</ul>"
    # return HttpResponse(response_data)

def monthly_challenges_by_numbers(request, month):
    try:
        months = list(challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("monthly-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>Invaild month</h1>")

def monthly_challenge(request, month):
    try:
        text = challenges[month]
        return render(request, "challenges_app/challenge.html", {"challenge_key": text, "month": month})
        # html_text = render_to_string("challenges_app/challenge.html")
        # return HttpResponse(html_text)
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    